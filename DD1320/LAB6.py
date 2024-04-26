import timeit
from del1_labb6 import read_songs_from_file
import random
from sökalgoritmer import linear_search, binary_search
from quicksort import quicksort
from indexqlist import IndexlistQ
from indexqlist import LinkedListQ
from bintreeFile import Bintree
from hashtable import Hashtable

if __name__ == "__main__":
    filename = "unique_tracks.txt"
    indexlist, songs_dictionary = read_songs_from_file(filename)

    # Teststorlekar
    n = [250000, 500000 , 1000000 ]
# Testfall I: Linjärsökning i osorterad indexlista för näst sista låten
    print("Testfall I: Linjärsökning i osorterad indexlista")
    print("--------------------------------------------------")
    for i in n:
        temp_indexlist=indexlist
        target = indexlist[-2]
        time = timeit.timeit(lambda: linear_search(temp_indexlist[:i], target), number=5)
        print(f"Tid för teststorlek {i}: {time}")

        #Tidskomplexitet: O(n)
        #   För varje element i listan måste alla element undersökas tills den näst sista låten hittas.

    # Testfall II: Linjärsökning i sorterad indexlista för näst sista låten
    print("\nTestfall II: Linjärsökning i sorterad indexlista")
    print("--------------------------------------------------")
    for i in n:
        temp_indexlist=indexlist[:i]
        sorted_indexlist = sorted(temp_indexlist, key=lambda x: (x.artist, x.title))
        target = sorted_indexlist[-2]
        time = timeit.timeit(lambda: linear_search(sorted_indexlist, target), number=5)
        print(f"Tid för teststorlek {i}: {time}")
    """Tidskomplexitet: O(n)
    Samma som ovan, även om listan är sorterad, krävs fortfarande att alla element undersöks för att hitta den näst sista låten."""
    # Testfall III: Linjärsökning i osorterad indexlista för slumpade låtar
    print("\nTestfall III: Linjärsökning i osorterad indexlista för slumpade låtar")
    print("---------------------------------------------------------------------")
    for i in n:
        temp_indexlist=indexlist[:i]
        random_target = random.sample(temp_indexlist, 1000)  # Slumpa 1000 låtar från index_list
        time = timeit.timeit(lambda: [linear_search(temp_indexlist, song) for song in random_target], number=5) / 1000
        print(f"Tid för teststorlek {i}: {time}")
    """Tidskomplexitet: O(n)
    Liknande som ovan, men eftersom låtarna är slumpade är det ingen garanti för att den näst sista låten är nära slutet av listan."""
    # Testfall IV: Sortering med quicksort
    print("\nTestfall IV: Sortering med quicksort")
    print("------------------------------------")
    for i in n:
        temp_indexlist=indexlist[:i]
        time = timeit.timeit(lambda: quicksort(temp_indexlist), number=5)
        print(f"Tid för teststorlek {i}: {time}")
    """Tidskomplexitet: O(n log n)
    Både heap-, merge- och quicksort har genomsnittlig tidskomplexitet på O(n log n) för att sortera n element."""
    # Testfall V: Binärsökning i sorterad indexlista
    print("\nTestfall V: Binärsökning i sorterad indexlista")
    print("------------------------------------------------")
    for i in n:
        temp_indexlist=indexlist[:i]
        sorted_indexlist = sorted(temp_indexlist, key=lambda x: (x.artist, x.title))
        target = sorted_indexlist[-2]
        time = timeit.timeit(lambda: binary_search(sorted_indexlist, target), number=5)
        print(f"Tid för teststorlek {i}: {time}")
    """Tidskomplexitet: O(log n)
    Binärsökning kan hitta ett element i en sorterad lista med logaritmisk tidskomplexitet."""
    # Testfall VI: Lägg in n element och ta bort dem i en IndexListQ
    print("\nTestfall VI: Lägg in n element och ta bort dem i en IndexListQ")
    print("----------------------------------------------------------------")
    for i in n:
        indexlistq = IndexlistQ()
        time = timeit.timeit(lambda: [indexlistq.enqueue(song) for song in indexlist[:i]], number=1)
        print(f"Tid för insättning av {i} element: {time}")
        time = timeit.timeit(lambda: [indexlistq.dequeue() for _ in range(i)], number=1)
        print(f"Tid för borttagning av {i} element: {time}")
    
    # Testfall VII: Lägg in n element och ta bort dem i en LinkedlistQ
    print("\nTestfall VII: Lägg in n element och ta bort dem i en LinkedlistQ")
    print("------------------------------------------------------------------")
    for i in n:
        linkedlistq = LinkedListQ()
        time = timeit.timeit(lambda: [linkedlistq.enqueue(song) for song in indexlist[:i]], number=1)
        print(f"Tid för insättning av {i} element: {time}")
        time = timeit.timeit(lambda: [linkedlistq.dequeue() for _ in range(i)], number=1)
        print(f"Tid för borttagning av {i} element: {time}")

    # Testfall VIII: Lägg in n element i ett binärträd
    print("\nTestfall VIII: Lägg in n element i ett binärträd")
    print("---------------------------------------------------")
    for i in n:
        bintree = Bintree()
        time = timeit.timeit(lambda: [bintree.store(song) for song in indexlist[:i]], number=1)
        print(f"Tid för insättning av {i} element: {time}")
    """Tidskomplexitet: O(n log n)
    Genomsnittlig tidskomplexitet för att lägga till n element i ett balanserat binärt sökträd är O(n log n)."""
    # Testfall IX: Lägg in n element i en Hashtabell
    print("\nTestfall IX: Lägg in n element i en Hashtabell")
    print("------------------------------------------------")
    for i in n:
        hashtable = Hashtable()
        time = timeit.timeit(lambda: [hashtable.store(song.trackid, song) for song in indexlist[:i]], number=1)
        print(f"Tid för insättning av {i} element: {time}")
    """Tidskomplexitet: O(n log n)
    Genomsnittlig tidskomplexitet för att lägga till n element i ett balanserat binärt sökträd är O(n log n)."""