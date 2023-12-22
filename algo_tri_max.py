# première méthode de tri, avec la boucle while
a_trier = [14, 12, 16, 8, 9, 10, 24, 21,108,104,2]


def triage():
    trier = []
    while len(a_trier) > 0:
        
        trier_max = max(a_trier)
        trier.append(trier_max)
        a_trier.remove(trier_max)
    return trier

print(triage())