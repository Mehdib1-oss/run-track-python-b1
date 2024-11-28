def echanger_premier_dernier(liste):
    if len(liste) > 0:
        liste[0], liste[-1] = liste[-1], liste[0]
    return liste

ma_liste = [10, 20, 30, 40, 50]
print("Avant échange:", ma_liste)
ma_liste = echanger_premier_dernier(ma_liste)
print("Après échange:", ma_liste)