from recherche import recherche
from remplace import remplace
from colorama import *

def color(prop,mot_tempo,resultat_tempo):
    """
    Cette fonction prend en argument une proposition prop, un mot mot_tempo et un autre resultat_tempo.
    Elle crée une copie en fonction des caractères de resultat_tempo, de mot_tempo et d'un autre caractère proposé prop.
    On fonction du caractère, celui-ci peut être coloré soit en bleu soit en rouge s'il est bien placé ou non.
    Elle retourne la copie resultat.
    """
    resultat=""
    for i in range(len(resultat_tempo)):
        if resultat_tempo[i]=="?":
            ind=recherche(mot_tempo,prop[i])
            if ind != -1:
                resultat=resultat+(Fore.BLUE+ prop[i] +Style.RESET_ALL)
                mot_tempo=remplace(mot_tempo,ind,"#")
            else:
                resultat=resultat+(Fore.RED + prop[i] + Style.RESET_ALL)
        else:
            resultat=resultat+(Fore.BLUE+ resultat_tempo[i] +Style.RESET_ALL)
    return resultat