from recherche import recherche
from remplace import remplace
from tkinter import *


def color(prop,mot_tempo,resultat_tempo):

    notif=Label(text="Le résultat est: ")
    notif.pack()
    resultat=""
    for i in range(len(resultat_tempo)):
        if resultat_tempo[i]=="?":
            ind=recherche(mot_tempo,prop[i])
            if ind != -1:
                prop[i]=prop[i].upper
                resultat=resultat+prop[i]
                mot_tempo=remplace(mot_tempo,ind,"#")
            else:
                prop[i]=prop[i].lower
                resultat=resultat+prop[i]
                
        else:
            resultat_tempo[i]=resultat_tempo[i].upper
            resultat=resultat+resultat_tempo[i]
    return resultat