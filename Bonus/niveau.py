import random
import codecs

def niveau (niveau_choisi):
    """
    Cette fonction prend en argument un mot niveau_choisi.
    Elle va chechercher aléatoirement un mot dans une liste donnée dans un fichier. 
    La taille du mot dépend de niveau_choisi. 
    Elle retourne le mot mot_alea.
    """
    mot_alea=""
    taille=26
    if niveau_choisi=="novice":
        while taille>5:
            mot_alea=random.choice(codecs.open("mots.txt",encoding="UTF-8").read().split())
            taille=len(mot_alea)

    elif niveau_choisi=="facile":
        while taille<6 or taille>10:
            mot_alea=random.choice(codecs.open("mots.txt",encoding="UTF-8").read().split())
            taille=len(mot_alea)

    elif niveau_choisi=="moyen":
        while taille<11 or taille>15:
            mot_alea=random.choice(codecs.open("mots.txt",encoding="UTF-8").read().split())
            taille=len(mot_alea)

    elif niveau_choisi=="difficile":
        while taille<16 or taille>20:
            mot_alea=random.choice(codecs.open("mots.txt",encoding="UTF-8").read().split())
            taille=len(mot_alea)

    elif niveau_choisi=="expert":
        while taille<21 or taille>25:
            mot_alea=random.choice(codecs.open("mots.txt",encoding="UTF-8").read().split())
            taille=len(mot_alea)

    return mot_alea