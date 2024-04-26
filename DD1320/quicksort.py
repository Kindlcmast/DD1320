def quicksort(list):
    if len(list) <= 1:  # Om listan har en eller inga element är den redan sorterad
        return list #Returnerar listan som  redan är sorterad
    pivot = list[len(list) // 2]  # Välj pivotelementet som mitten av listan
    left = [x for x in list if x < pivot]  # Dela upp listan i mindre än pivotelementet
    middle = [x for x in list if x == pivot]  # Dela upp listan i element som är lika med pivotelementet
    right = [x for x in list if x > pivot]  # Dela upp listan i större än pivotelementet
    return quicksort(left) + middle + quicksort(right)  # Kombinera de sorterade delarna av listan

if __name__ == "__main__":
    # Testa funktionen genom att sortera en lista
    testlist = [3, 6, 8, 10, 1, 2, 1]
    sortedlist = quicksort(testlist)  # Anropa quicksort-funktionen för att sortera listan
    print("Sorted list:", sortedlist)  # Skriv ut den sorterade listan
