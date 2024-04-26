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
    def __init__(self, tal):
        # Skapar en nod med det angivna värdet tal och en pekare till nästa nod
        self.tal = tal
        self.next = None

class LinkedListQ:
    def __init__(self):
        # Skapar en tom länkad lista med både head och tail
        self.head = None
        self.tail = None
    def isEmpty(self):
        # Returnerar True om kön är tom, annars False
        return self.head is None
    
    def enqueue(self, tal):
        # Lägger till ett element i slutet av den länkade listan
        nyNode = Node(tal)
        if self.head is None:
            # Om kön är tom, sätt både head och tail till den nya noden
            self.head = nyNode
            self.tail = nyNode
        else:
            # Annars lägg till den nya noden efter den befintliga sista noden (tail)
            self.tail.next = nyNode
            self.tail = nyNode

    def dequeue(self):
        # Tar bort och returnerar det första elementet i den länkade listan
        if self.head is None:
            return None
        
        x = self.head.tal
        self.head = self.head.next
        
        # Om kön blir tom efter borttagning, sätt tail till None också
        if self.head is None:
            self.tail = None
        return x

    def remove(self, tal):
        # Tar bort alla noder med det angivna värdet tal från den länkade listan
        bakom = None
        framför = self.head

        # Ta bort alla förekomster av tal från början av kön
        while framför is not None:
            if framför.tal == tal:
                if bakom is None:  # Om noden med tal är den första noden
                    self.dequeue()
                    framför = self.head
                else:
                    bakom.next = framför.next
                    # Uppdatera tail om den borttagna noden är den sista noden
                    if framför == self.tail:
                        self.tail = bakom
                    framför = framför.next
            else:
                bakom = framför
                framför = framför.next

def basictest():
    q = LinkedListQ()
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
    e=LinkedListQ()
    e.enqueue(x1)
    e.enqueue(x2)
    e.enqueue(x3)
    e.remove(x2)
    x1=e.dequeue()
    x2=e.dequeue()
    x3=e.dequeue()
    print(x1)
    print(x2)
    print(x3)
if __name__ == "__main__": 
    basictest()