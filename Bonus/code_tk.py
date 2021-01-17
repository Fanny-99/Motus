from tkinter import *
from bien_place import bien_place
from cache_lettre import cache_lettre
from newresult import newresult
from niveau import niveau
from couleur import color
import csv
import random
import codecs
from novice_tk import *
from facile_tk import *
from moyen_tk import *
from difficile_tk import *
from expert_tk import *

# window=Tk()
# window.title("Motus")

# def intro1():
#     for w in window.winfo_children():
#         w.destroy()
#     intro1=Label(window,text="Bienvenue Joueur/Joueuse!\n... Hmmmm peut-être un peu trop formel comme message de salutations.\nJe me présente, je suis Motus, un jeu qui reprend le même principe que celui de l'émission télé.\nSi si, vous savez! Le jeu télé qui était présenté par Thierry Beccaro!\nVous ne le connaissez pas?\nMoi non plus.\nBref! Maintenant que je me suis présenté, c'est à votre tour!\nComment vous appelez-vous donc, cher Joueur/Joueuse ?\n\nNom:")
#     nom=StringVar()
#     nom.set("")
#     entry=Entry(window,textvariable=nom)
#     intro1.pack()
#     entry.pack()

#     def name1():
#         intro=Label(window,text="Ravi de faire votre connaissance, " +entry.get()+ " ! \nA présent, si nous commencions à jouer?\nNous allons faire ensemble 5 parties successives de Motus.\nA chaque fois, vous pourrez choisir votre niveau de difficulté, et vous disposerez de 6 essais pour chaque mot à trouver.\nEn fonction du nombre d'essais qu'il vous aura fallu pour trouver le mot et de la difficulté, vous vous verrez attribuer un score.\nChaque score obtenu augmentera votre score total.\nAttention toutefois à ne pas viser trop haut si vous voulez marquer des points!")
#         intro.pack()
#         bouton_continuer=Button(window,text="continue",command=continuer)
#         bouton_continuer.pack()

#     done=Button(window,text="Done",command=name1)
#     done.pack()


# def intro2():
#     for w in window.winfo_children():
#         w.destroy()
#     intro2=Label(window,text="Veuillez entrer votre nom s'il vous plaît:")
#     nom=StringVar()
#     nom.set("")
#     entry=Entry(window,textvariable=nom)
#     intro2.pack()
#     entry.pack()

#     def name2():
#         intro=Label(window,text="Amusez-vous bien "+entry.get()+" !")
#         intro.pack()
#         bouton_continuer=Button(window,text="continue",command=continuer)
#         bouton_continuer.pack()

#     done=Button(window,text="Done",command=name2)
#     done.pack()


# def continuer():
#     window.destroy()




# widget=Label(window,text="Bonjour! Souhaitez-vous visionner l'introduction ?\nRépondez par oui ou par non.")
# widget.pack()

# bouton_oui=Button(window,text="oui",command=intro1)
# bouton_oui.pack()

# bouton_non=Button(window,text="non",command=intro2)
# bouton_non.pack()

# window.mainloop()




window2=Tk()
window2.title("Motus")

niveaux=Label(window2,text="Les différents niveaux sont:\n\n-novice (mot de 1 à 5 lettres)\n-facile (mot de 6 à 10 lettres)\n-moyen (mot de 11 à 15 lettres)\n-difficile (mot de 16 à 20 lettres)\n-expert (mot de 21 à 25 lettres)")
niveaux.pack()

def novice_bis():
    for w in window2.winfo_children():
        w.destroy()
    bouton_continuer=Button(window2,text="continue",command=novice)
    bouton_continuer.pack()

choix=Label(window2,text="Choisissez un niveau:")
choix.pack()

bouton_novice=Button(window2,text="novice", command=novice_bis)
bouton_novice.pack()


bouton_facile=Button(window2,text="facile", command=facile)
bouton_facile.pack()

bouton_moyen=Button(window2,text="moyen", command=moyen)
bouton_moyen.pack()

bouton_difficile=Button(window2,text="difficile", command=difficile)
bouton_difficile.pack()

bouton_expert=Button(window2,text="expert", command=expert)
bouton_expert.pack()



window2.mainloop()



