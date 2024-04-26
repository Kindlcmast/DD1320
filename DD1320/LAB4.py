import string
import sys
from hashtable import Hashtable
from indexqlist import LinkedListQ
##________________uppgift1_________________________

# Funktionen makechildren1() genererar alla möjliga barnord för ett givet ord genom att byta ut en bokstav i taget.
def makechildren1(ord):
    # Skapar en sträng med det svenska alfabetet, inklusive å, ä och ö.
    alfabet = string.ascii_lowercase + 'åäö'
    # Skapar en tom lista för att lagra de genererade barnorden.
    barnen = []  

    # Loopar över varje position i det givna ordet.
    for i in range(len(ord)):
        # Loopar över varje bokstav i det svenska alfabetet.
        for bokstav in alfabet:
            # Genererar ett barnord genom att byta ut bokstaven på den aktuella positionen.
            barn = ord[:i] + bokstav + ord[i+1:]
            # Kontrollerar att det genererade barnordet inte är identiskt med föräldern och inte redan finns i listan.
            if barn != ord and barn not in barnen:
                # Lägger till det genererade barnordet i listan över barnord.
                barnen.append(barn)
    # Returnerar listan över alla genererade barnord.
    return barnen

def testUppgift1():
    ord = "ok"
    # Beräkna det förväntade antalet barn för det givna ordet
    antal = len(string.ascii_lowercase + 'åäö') * len(ord) - len(ord)  # Antalet möjliga barnord
    antalBarn = makechildren1(ord)
    # Kontrollera om antalet genererade barn överensstämmer med det förväntade antalet
    
    if antal==len(antalBarn):
        print("Test 1 ok!")
    else:
        print("Test 1 fail")    


##_________________Uppgift 2_____________________
def makechildren2(ord, ordTree):
    alfabet = string.ascii_lowercase + 'åäö'  # Svenska alfabetet
    barnen = [] # Skapar en tom lista för att lagra de genererade barnorden.

    # Loopa över varje bokstav i det givna ordet
    for i in range(len(ord)):
        # Loopa över varje bokstav i det svenska alfabetet
        for bokstav in alfabet:
            # Byt ut en bokstav i taget och skapa ett nytt ord
            barn = ord[:i] + bokstav + ord[i+1:]
            # Lägg till det nya ordet i listan över barnord om det finns i ordlistan och inte är identiskt med föräldern
            if barn != ord and barn not in barnen and ordTree.__contains__(barn):
                barnen.append(barn)

    return barnen

def LasFranFil(filnamn):
    ordTree = Hashtable()
    # Öppna filen för läsning och läs varje ord
    with open(filnamn, 'r', encoding='utf-8') as fil:
        for rad in fil:
            # Ta bort eventuella whitespace-tecken från början och slutet av raden för att få ordet
            ord = rad.strip()
            # Lagra ordet i det binära sökträdet
            ordTree.store(ord)
    return ordTree

# Testa funktionen
def testUppgift2():
    # Definiera ett startord
    ord = "fan"
    # Läs in giltiga ord från filen och skapa ett binärt sökträd
    ordTree = LasFranFil("Word3.txt")
    # Generera barnord för det givna startordet
    genereradeBarn = makechildren2(ord, ordTree)
    forvantatantal = 17   #från uppgiften ska det endast finnas 17st
    # Kontrollera om antalet genererade barnord överensstämmer med det förväntade antalet
    
    if len(genereradeBarn)==forvantatantal:
        print("Test 2 ok!")
    else:
        print("Test 2 fail")  

#__________________________uppgift 3________________________________

def makechildren3(ord, ordTree, besoktaTree):

    """Tar in tre args 
    ord - startordet som det genereras nya ord kring 
    ordTree - ett träd med samtliga giltiga ord
    besoktaTree - ett trädm med redan besökta träd
    genererar nya ord genom att byta ut en boksatv i ord i taget
    returnerar en lista med nya generarade ord från det ginva ord"""
    alfabet = string.ascii_lowercase + 'åäö'  # Svenska alfabetet
    barnen = [] # Skapar en tom lista för att lagra de genererade barnorden.
    
    # Loopa över varje bokstav i det givna ordet
    for i in range(len(ord)):
        # Loopa över varje bokstav i det svenska alfabetet
        for bokstav in alfabet:
            # Byt ut en bokstav i taget och skapa ett nytt ord
            barn = ord[:i] + bokstav + ord[i+1:] #ett nytt ord där vi har bytt ut den aktuella bokstaven på position i mot en annan bokstav från det svenska alfabetet.
            # Lägg till det nya ordet i listan över barnord om det är giltigt, inte identiskt med föräldern och inte tidigare har besökts
            if ordTree.__contains__(barn) and barn != ord and not besoktaTree.__contains__(barn):
                barnen.append(barn)
                besoktaTree.store(barn)  # Markera barnet som besökt
    return barnen

# Testa funktionen
def testUppgift3():
    besoktaTree = Hashtable()  # Skapa ett tomt träd för besökta ord
    besoktaTree.store("fin")
    startOrd = "fan"
    ordTree = LasFranFil("Word3.txt")
    generaradeBarn = makechildren3(startOrd, ordTree, besoktaTree)
    forvantatAntal = 16  # Antalet unika giltiga barnord för ordet "fin" (fan ska inte genereras eftersom den redan besökts)
    if len(generaradeBarn)==forvantatAntal:
        print("Test 3 ok!")
    else:
        print("Test 3 fail")  


#_________________________uppgift 4_______________________

def finnsVagen(startOrd, slutOrd, ordTree):
    besoktaTree = Hashtable()  # Skapa ett tomt träd för besökta ord
    queueOfWords = LinkedListQ() 
    queueOfWords.enqueue(startOrd)  # Lägg till startordet i kön

    while not queueOfWords.isEmpty():
        nastaOrd = queueOfWords.dequeue()  # Ta ut det första ordet ur kön
        if nastaOrd == slutOrd:  # Om vi har nått slutordet, returnera True (vi har hittat en väg)
            return True
        
        for barn in makechildren3(nastaOrd, ordTree,besoktaTree):
            queueOfWords.enqueue(barn)  # Lägg till alla giltiga barnord i kön
            besoktaTree.store(barn)  # Markera barnet som besökt

    return False  # Om kön är tom fanns ingen väg

# Testa funktionen
def testUppgift4():
    startOrd = "fan"
    slutOrd = "gud"
    ordTree = LasFranFil("Word3.txt")  # Läs in ord från en fil och lagra dem i ett binärt sökträd

    if finnsVagen(startOrd, slutOrd, ordTree):
        print(f"Det finns en väg mellan {startOrd} och {slutOrd}.")
    else:
        print(f"Det finns ingen väg mellan {startOrd} och {slutOrd}.")


#______________________________uppgift 5___________________________
# Klass för föräldranoder
class ParentNode:
    def __init__(self, ord, foralder=None):
        self.ord = ord
        self.foralder = foralder

"""          fan
           /  |  \
          /   |   \
       fin   man   far
      / | \  / \   / \
     /  |  \/   \ /   \
   hin  din hun mun var
    fan = ParentNode("fan")  # Startnoden, ingen förälder
fin = ParentNode("fin")
man = ParentNode("man")
far = ParentNode("far")
hin = ParentNode("hin")
din = ParentNode("din")
hun = ParentNode("hun")
mun = ParentNode("mun")
var = ParentNode("var")

fan.foralder = None
fin.foralder = fan
man.foralder = fan
far.foralder = fan
hin.foralder = fin
din.foralder = fin
hun.foralder = fin
mun.foralder = man
var.foralder = far

   """

def breddenforstsokning(startOrd, slutOrd, ordTree):
    besoktaTree = Hashtable()  # att spåra besökta ord
    q = LinkedListQ()  #skapar en kö för ord att kolla på
    startNod = ParentNode(startOrd)  # Skapa en startnod för att spara vägen till slutordet
    q.enqueue(startNod)  # Lägg till startnoden i kön

    while not q.isEmpty():
        tempNod = q.dequeue()  # Ta bort första noden/barnnoden från kön

        if tempNod.ord == slutOrd:  # Om vi hittar slutordet, returnera noden
            return tempNod
        besoktaTree.store(tempNod.ord)  # Lägg till det nuvarande ordet i besökt lista
        
        barnen = makechildren3(tempNod.ord, ordTree, besoktaTree)  # Skapa barn för det nuvarande ordet
        for barn in barnen:
            barnNod = ParentNode(barn, tempNod)  # Skapa en nod för barnet med referens till föräldernoden
            q.enqueue(barnNod)  # Lägg till barnnoden i kön

    return None  # Om ingen väg hittades, returnera None

# Funktion för att skriva ut hela vägen från startnoden till slutnoden
def writechain(node):
    if node is None:
        return #finns inget mer att skriva ut
    writechain(node.foralder)  # Fortsätt rekursivt till föräldernoden
    print(node.ord)  # Skriv ut ordet


def main():
    # Testa uppgift 1
    testUppgift1()
    # Testa uppggift 2
    testUppgift2()
    # Testa uppgift 3
    testUppgift3()
    # Testa uppgift 4 
    testUppgift4()
    
    if len(sys.argv) < 3:
        print("Start- och slutord saknas")
        print("Använd programmet så här: \n\t python3", sys.argv[0], " [startord] [slutord]")
        sys.exit()

    startOrd = sys.argv[1]
    slutOrd = sys.argv[2]
    filnamn="Word3.txt"
    ordTrad = LasFranFil(filnamn)  # Skapa ett binärt sökträd för att lagra giltiga ord
    slutNod = breddenforstsokning(startOrd, slutOrd, ordTrad)

    if slutNod: #om slutnoden inte är none finns det en väg
        print("Vägen mellan", startOrd, "och", slutOrd, "är:")
        writechain(slutNod)  # Skriv ut hela vägen från startnoden till slutnoden
    else:
        print("Det finns ingen väg mellan", startOrd, "och", slutOrd)
if __name__ == "__main__":
    main()


    
   