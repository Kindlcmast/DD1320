from indexqlist import LinkedListQ as ko
def trolleritrick( siffror ):
    trolleri_ordning = []
    q=ko()
    for i in range(len(siffror)):
        q.enqueue(siffror[i]) #lägger in samtliga siffror i kön
    while not q.isEmpty():
        #tar ut varannan, stoppar tillbaka varannan
        q.enqueue(q.dequeue()) 
        trolleri_ordning.append(q.dequeue())
    
    return trolleri_ordning

import sys
def main():
    """
    #line = input("Vilken ordning ligger korten i?")
    line = "3   1   4   2   5 "
    siffror = line.strip().split()
    trollning = trolleritrick( siffror )
    print("De kommer i följande ordning: ", end="")
    for x in trollning:
        print(x, end=" ")
    print()
    
    """
    #siffror = sys.stdin.readline()
    #lösning = trolleritrick(siffror.strip())
    #print(lösning)
    
    line = sys.stdin.readline()
    siffror = line.strip().split()
    trollning = trolleritrick( siffror )
    print(siffror)
    for x in trollning:
        print(x, end=" ") 
        print() #"""
    
    
    
    #Vilken ordning ligger korten i? 
    #3   1   4   2   5 
    #De kommer ut i denna ordning: 1 2 3 5 4

    #echo 3 1 4 2 5  | python3 Trolleri.py
if __name__ == "__main__": 
    main()