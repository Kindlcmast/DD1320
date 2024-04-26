

class IndexlistQ:
    def __init__(self):
        #skapar en tom lista
        q=[]
        self.q=q
    def enqueue(self, x):
        #för att stoppa in något i kö
        self.q.append(x)
    def dequeue(self):
        #tar ut det första ur listan
        y=self.q[0]
        self.q.pop(0)
        return y
    def isEmpty(self):
        # Returnerar True om den länkade listan är tom, annars False
        return not bool(self.q)
    
    def __str__(self):
        #För utskrift
        return f"{self.q}"


class Node:
    # Node-klassen: Den representerar varje enskild nod i den länkade listan. 
    # Varje nod har två attribut: tal för att lagra värdet och next för att peka på nästa nod i listan.
    def __init__(self, tal):
       #tal är det numeriska värdet som noden ska lagra, och next är en pekare till nästa nod i listan.
        self.tal = tal
        self.next = None
        

    
class LinkedListQ:
    #LinkedListQ-klassen: Denna klass representerar själva köstrukturen som bygger på den länkade listan.
    def __init__(self):
         # Skapar en tom länkad lista
        self.head = None
    
    def __str__(self):
        # Returnerar en strängrepresentation av den länkade listan
        return f"{self.head}"
    
    def enqueue(self, tal):
        # Lägger till ett element i slutet av den länkade listan
        nyNode = Node(tal) #Detta objekt representerar det nya elementet som ska läggas till i kön.
        if self.head is None: #Om self.head är None, betyder det att listan är tom och att det nya elementet ska placeras först i kön.
            self.head = nyNode # self.head tilldelas den nya noden nyNode, vilket innebär att den blir den enda noden i kön.
            return
    
        tempNode = self.head
        while(tempNode.next): #: itererar genom kön tills den sista noden i listan har hittats. sjukt oeffektivt så här i efterhand
            tempNode = tempNode.next
        tempNode.next = nyNode
        #Skulle kanske egentligen implememnterat en pekare till slutet av kön i klassen Node, för att slippa gå igenom hela kön för att hitta den sista platsen
        return
    
    def dequeue(self):
        # Tar bort och returnerar det första elementet i den länkade listan
        if(self.head == None): #kontroll för att se om kön är tom.
            return
        x=self.head.tal #Om kön inte är tom, tilldelas värdet av det första elementet i kön 
        self.head = self.head.next # Det första elementet i kön tas bort genom att ändra self.head till att peka på nästa nod i listan.
        return x

    def isEmpty(self):
        # Returnerar True om den länkade listan är tom, annars False
        return not bool(self.head)

    def remove(self, tal):
        # Tar bort en nod med det angivna värdet tal från den länkade listan
        tempNode = self.head #En temporär nod tempNode skapas och pekar till attbörja med på den första noden
    
        if tempNode.tal == tal: #kontroll för att se om det första noden i listan har det angivna värdet tal. 
            self.dequeue()    
        while tempNode is not None and tempNode.next.tal != tal:
            tempNode = tempNode.next
    
        if tempNode is None:
            return
        else:
            tempNode.next = tempNode.next.next #ändrar pekaren från den aktuella noden (tempNode) till att hoppa över nästa nod och istället peka på nästa-nästa nod.
            return
        

    """def mintestdfunkion():
        q=[]
        q = IndexlistQ(q)
        if q.isEmpty():
            print("den är tom")
        else:
            print("den är inte tom")
        q.enqueue(3)
        x=q.dequeue()
        print(x)
        w=[]
        w=IndexlistQ(w)
        x1=1
        x2=2
        x3=3
        w.enqueue(x1)
        w.enqueue(x2)
        w.enqueue(x3)

        if w.isEmpty():
            print("den är tom")
        else:
            print("den är inte tom")
        x1=w.dequeue()
        x2=w.dequeue()
        x3=w.dequeue()
        if x1<x2<x3:
            print("ok")"""


def basictest():
    q = IndexlistQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()

    # Förväntat resultat
    if (x == 1 and y == 2 and q.isEmpty()):
        print("test OK")
    else:
        print("FAILED expected x=1 and y=2 and an empty list but got x =", x, " y =", y, " and empty list is", q.isEmpty())

    print('går vidare till del två')

    """    Söka efter och ta bort det mittersta elementet i en kö med tre noder
    Ta bort första elementet i en kö med en nod
    Försök ta bort ett element som inte finns i en kö med några noder (kön ska förbli oförändrad)
    Försök ta bort ett  element ur en tom kö (inget ska hända och programmet ska inte krascha)
    Ta bort sista elementet i en kö med några noder
    """

    q = LinkedListQ()
    if q.isEmpty():
        print("den är tom")
    else:
        print("den är inte tom")
    x=q.dequeue
    q.enqueue(3)
    x=q.dequeue()
    print(x)
    print('förväntat:  3')
    w=LinkedListQ()
    x1=1
    x2=2
    x3=3
    w.enqueue(x1)
    w.enqueue(x2)
    w.enqueue(x3)

    if w.isEmpty():
        print("den är tom")
    else:
        print("den är inte tom")
    x1=w.dequeue()
    x2=w.dequeue()
    x3=w.dequeue()
    if x1<x2<x3:
        print("ok")
    w.enqueue(x1)
    w.enqueue(x2)
    w.enqueue(x3)
    w.enqueue(x3)

    x1=w.dequeue()
    x2=w.dequeue()
    x3=w.dequeue()

    if x1<x2:
        print("ok")
if __name__ == "__main__": 
    basictest()

