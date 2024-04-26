import json
import re
import random
import csv
class Pokemon:
    def __init__(self, data, msg, sp_msg):
        self.id = int(data["id"])
        self.name = data["name"]["english"]
        self.type = data["type"]
        self.hp = data["base"]["HP"]
        self.attack = data["base"]["Attack"]
        self.defense = data["base"]["Defense"]
        self.sp_attack = data["base"]["Sp_Attack"]
        self.sp_defense = data["base"]["Sp_Defense"]
        self.speed = data["base"]["Speed"]
        self.level = 1
        self.msg = msg
        self.sp_msg = sp_msg

    def __str__(self):
        return f"{self.name.capitalize()}"

    def __lt__(self, other):
        if self.hp != other.hp:
            return self.hp < other.hp
        return self.id < other.id

class Pokedex:
    def __init__(self):
        self.attack_messages = self.extract_attack_messages() 
        self.pokemon_dict = load_pokedex(self)
        self.type_effectiveness=self.load_type_effectiveness()

    def extract_attack_messages(self):
        attack_msg = []
        file="List_of_moves_mod.html"
        with open(file, "r", encoding="utf-8") as file:
            junk = file.read()
            msgs = re.findall(r"<td><small>(.*?)</small>", junk)
            for msg in msgs:
                short_msg = msg.split(".")[0]
                attack_msg.append(short_msg.strip())
        return attack_msg
    
    def load_type_effectiveness(self):
        with open('statchart.csv', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            types = next(reader)
            type_effectiveness = {}
            
            # itererar över varje typ 
            for i, row in enumerate(reader):
                # den aktuella attacktypen
                attack_type = types[i]
                effectiveness_dict = {}
                
                # effektiviteten för attacktypen mot varje försvarstyp
                for j, eff in enumerate(row):
                    defender_type = types[j]
                    effectiveness_dict[defender_type] = float(eff)
                    
                type_effectiveness[attack_type] = effectiveness_dict
                """{
                    "Normal": {"Normal": 1.0, "Fire": 0.5, "Water": 2.0},
                    "Fire": {"Normal": 2.0, "Fire": 1.0, "Water": 0.5}
                }"""

        return type_effectiveness   
     
    def type_modifier(self, attacker, defender):
        attacker_type = attacker.type[0]
        modifier = 1.0 
        
        for defender_type in defender.type:
            try:
                modifier = modifier* self.type_effectiveness[attacker_type].get(defender_type, 1) #multiplicerar för varje typ som den har   
            except KeyError:
               #påverkar inte modifier).
                pass
        
        return modifier


    def move(self, p1, p2, special = False):
        # dmg = ((2A/5+2)*B*C)/D)/50)+2)*X)*Y/10)*Z)/255
        # A = attacker's Level
        # B = attacker's Attack or Special defense
        # C = attack Power
        # D = defender's Defense or Special defense
        # X = same-Type attack bonus (1 or 1.5)
        # Y = Type modifiers (40, 20, 10, 5, 2.5, or 0)
        # Z = a random number between 217 and 255
        A = p1.level
        B = p1.sp_attack if special else p1.attack
        C = B
        D = p1.sp_defense if special else p1.defense
        X = 1
        Y = self.type_modifier(p1, p2)
        Z = random.randint(217, 255)
        dmg = (((((((2*A/5+2)*B*C)/D)/50)+2)*X*Y)*Z)/255
        return dmg
    

    
    def __getitem__(self, key):
        try:
            key = key.lower()  
        except AttributeError:
            key = str(key)  

        try:
            pokemon=self.pokemon_dict[key]

            return pokemon
        except KeyError:
            print(f"Pokémon with name/id '{key}' not found.")
    
    def random_opponent(self, pokemon):
        p_opp = []
        # Iterera över alla Pokémons i pokedex i pokemon_dict
        for opp in self.pokemon_dict.values():
            same_type = False
            for type in opp.type:
                if type in pokemon.type:
                    same_type = True
                    break  # Bryter loopen om en gemensam typ hittas
            # Om ingen gemensam typ hittades
            if not same_type:
                p_opp.append(opp)
        return random.choice(p_opp) if p_opp else None
    
def load_pokedex(self):
    with open("pokedex.json", "r") as pokefile:
        data = json.load(pokefile)
    pokemon_dict = {}
    for pokemon_data in data:
        msg, sp_msg = random.sample(self.attack_messages, 2)
        pokemon = Pokemon(pokemon_data, msg, sp_msg)
        pokemon_dict[pokemon.name.lower()] = pokemon
        pokemon_dict[str(pokemon.id)] = pokemon
    return pokemon_dict

def main():
    pokedex = Pokedex()
    p1 = pokedex[1]
    p2 = pokedex["1"]
    p3 = pokedex["bulbasaur"]
    p4 = pokedex["Bulbasaur"]

    if p1 == p2 == p3 == p4:
        print("___getitem__ OK")

    poke = pokedex["Pikachu"]
    if poke:
        opponent = pokedex.random_opponent(poke)
        if opponent:
            print(f"{poke.name} against {opponent.name}")
        else:
            print(f"opponent nott found for {poke.name}")
    else:
        print("not found")
if __name__ == "__main__":
    main()
