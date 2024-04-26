#uppgift 1
import json
import re
from Pokedex import Pokemon

def load_pokedex():
    with open("pokedex.json", "r") as fil:
        pokelist = json.load(fil)
    pokedict = {}
    for pokemon in pokelist:
        pokedict[pokemon["name"]["english"].lower()] = pokemon

    return pokedict

# Ladda pokedex från JSON-filen
pokedex = load_pokedex()

# Kolla att du kan komma åt 'id' och 'defense' för Pikachu

print("Test uppgift 1")
pikachu = pokedex.get("pikachu")
if pikachu:
    print("Pikachu's ID:", pikachu.get("id"))
    print("Pikachu's defense:", pikachu.get("base", {}).get("Defense"))
else:
    print("Pikachu not found in the Pokedex.")
print("_________________________")


#uppgift 2.1

def extract_attack_messages():
    attack_messages = []
    html_file="List_of_moves_mod.html"
    with open(html_file, "r", encoding="utf-8") as file:
        html_content = file.read()  
        # Använd reguljära uttryck för att hitta alla rader som börjar med "<td><small>"
        matches = re.findall(r"<td><small>(.*?)</small>", html_content)
        # Gå igenom matchningarna och spara bara första meningen i varje meddelande
        for match in matches:
            # Använd punkt som avgränsare för att dela upp meddelandet och behåll bara första delen
            first_sentence = match.split(".")[0]
            attack_messages.append(first_sentence.strip())  # Ta bort eventuella extra mellanslag
    return attack_messages

# Testa funktionen med att extrahera attackmeddelandena från HTML-filen
#attack_messages = extract_attack_messages("List_of_moves_mod.html")
#print("Antal attackmeddelanden:", len(attack_messages))
#print("Exempel på några attackmeddelanden:")
#for i in range(len(attack_messages)):
#    print(f"{i+1}. {attack_messages[i]}")


def main():
    # Ladda din Pokedex
    pokedex = load_pokedex()

    # Skapa två Pokémon-objekt
    pikachu_data = pokedex.get("pikachu")
    charmander_data = pokedex.get("charmander")

    pikachu = Pokemon(pikachu_data)
    charmander = Pokemon(charmander_data)

    # Testa __str__ metoden
    print(str(pikachu))  # Förväntat: Pikachu
    print(str(charmander))  # Förväntat: Charmander

    # Testa __lt__ metoden
    if pikachu < charmander:
        print(f"{pikachu} har mindre HP än {charmander}.")
    else:
        print(f"{charmander} har mindre HP än {pikachu}.")

if __name__ == "__main__":
    main()
    