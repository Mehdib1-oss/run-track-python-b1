def my_long_word(nombre, phrase):
    mots_plus_longs = []
    
    mots = phrase.split(" ")
    
    for mot in mots:
        compteur = 0
        for lettre in mot:
            compteur += 1  
        
        if compteur > nombre:
            mots_plus_longs.append(mot)
    
    return " ".join(mots_plus_longs)

phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, phrase)
print("Mots plus longs que 3 :", resultat)
