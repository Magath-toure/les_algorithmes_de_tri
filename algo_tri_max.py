import time

# première méthode de tri, avec la boucle while
a_trier = [14, 12, 16, 8, 9, 10, 24, 21, 108, 104, 2]

def tri_1():
    start_time = time.time()
    trier = []
    while len(a_trier) > 0:
        
        trier_max = max(a_trier)
        trier.append(trier_max)
        a_trier.remove(trier_max)

    end_time = time.time()

    print(f"Temps exécution TRI 1 = {end_time - start_time}") 
    return trier

def tri_2():
    start_time = time.time()
    # parcourir le tableau de manière globale
    for i in range(0, len(a_trier)):
        # parcourir le reste du tableau pour comparaison
        for j in range(0, len(a_trier[i+1:])):
            # quand le nombre qui se trouve en j est + grand
            # alors permuter avec le nombre en i
            if a_trier[i] < a_trier[i + j]:
               temp_value = a_trier[i]
               a_trier[i] = a_trier[i + j]
               a_trier[i + j] = temp_value

    end_time = time.time()

    print(f"Temps exécution TRI 2 = {end_time - start_time}") 
    return a_trier

def tri_3():
    start_time = time.time()
    max_i = len(a_trier) - 1
    continue_tri = True

    while continue_tri:
        continue_tri = False
        for i in range(max_i):
            if a_trier[i] > a_trier[i+1]:
                # permutation des valeurs qui se trouvent dans i et i+1
                a_trier[i], a_trier[i+1] = a_trier[i+1], a_trier[i]
                continue_tri = True
        max_i -= 1

    end_time = time.time()
    print(end_time - start_time)
    return a_trier

#print(tri_1())
#print(tri_2())
#print(tri_3())
