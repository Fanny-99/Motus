from recherche import recherche
from remplace import remplace

def newresult(prop,mot_tempo,resultat_tempo):
    """
    Cette fonction prend en argument une proposition prop, un mot mot_tempo et un autre resultat_tempo.
    Elle crée une copie en fonction des caractères de resultat_tempo, de mot_tempo et d'un autre caractère proposé prop.
    Elle retourne la copie resultat.
    """
    resultat=""
    for i in range(len(resultat_tempo)):
        if resultat_tempo[i]=="?":
            ind=recherche(mot_tempo,prop[i])
            if ind != -1:
                resultat=resultat+prop[i]
                mot_tempo=remplace(mot_tempo,ind,"#")
            else:
                resultat=resultat+prop[i]
        else:
            resultat=resultat+resultat_tempo[i]
    return resultat