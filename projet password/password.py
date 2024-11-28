import hashlib
import re
import json
import os

def verifier_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractères."
    if not re.search(r'[A-Z]', mot_de_passe):
        return False, "Le mot de passe doit contenir une majuscule."
    if not re.search(r'[a-z]', mot_de_passe):
        return False, "Le mot de passe doit contenir une minuscule."
    if not re.search(r'[0-9]', mot_de_passe):
        return False, "Le mot de passe doit contenir un chiffre."
    if not re.search(r'[!@#$%^&*]', mot_de_passe):
        return False, "Le mot de passe doit contenir un caractère spécial (!, @, #, $, %, ^, &, *)."
    return True, "Mot de passe valide."

def crypter_mot_de_passe(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

def lire_mots_de_passe():
    if os.path.exists('mots_de_passe.json'):
        with open('mots_de_passe.json', 'r') as f:
            return json.load(f)
    else:
        return {}

def ajouter_mot_de_passe(mot_de_passe_crypte):
    mots_de_passe = lire_mots_de_passe()
    mots_de_passe[mot_de_passe_crypte] = True  
    with open('mots_de_passe.json', 'w') as f:
        json.dump(mots_de_passe, f, indent=4)

while True:
    mot_de_passe = input("Entrez un mot de passe sécurisé (ex : MonMotDePasse1@) : ")
    valide, message = verifier_mot_de_passe(mot_de_passe)

    if valide:
        mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe)
        
        mots_de_passe_enregistres = lire_mots_de_passe()

        if mot_de_passe_crypte in mots_de_passe_enregistres:
            print("Ce mot de passe a déjà été utilisé, veuillez en choisir un autre.")
        else:
            print("Mot de passe validé et crypté.")
            ajouter_mot_de_passe(mot_de_passe_crypte)
            break
    else:
        print(f"Erreur : {message}")
