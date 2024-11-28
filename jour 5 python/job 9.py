def trouver_max_min(liste):
    maximum = max(liste)
    minimum = min(liste)
    return maximum, minimum

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
max_val, min_val = trouver_max_min(L)
print("La valeur maximale est:", max_val)
print("La valeur minimale est:", min_val)
