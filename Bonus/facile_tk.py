from tkinter import *
from bien_place import bien_place
from cache_lettre import cache_lettre
from newresult import newresult
from niveau import niveau
from couleur_tk import color


def facile():
    niveau_choisi="facile"
    mot_alea=niveau(niveau_choisi)
    taille=str(len(mot_alea))
    premiere_lettre=mot_alea[0]
    mot_aleat=Label(text="Entrer un mot de "+ taille +" lettres dont la première est "+ premiere_lettre +" :")
    mot=StringVar()
    mot.set("")
    mot=Entry(textvariable=mot)
    mot_propo=str(mot.get())
    mot_aleat.pack()
    mot.pack()
 
        
    def essai1():
        mot_propo=mot.get()
        gagne=False
        resultat_tempo=bien_place(mot_alea,mot_propo)
        mot_tempo=cache_lettre(mot_alea,resultat_tempo)
        reponse=newresult(mot_propo,mot_tempo,resultat_tempo)

        if reponse==mot_alea:
            gagne=True
            reponse_color=color(mot_propo,mot_tempo,resultat_tempo)
            resultat=Label(text="Le résultat est: "+reponse_color)
            message=Label(text="Vous avez gagné !!!")
            score_partie=Label(text="Votre score est de: 300 points.")
            resultat.pack()
            message.pack()
            score_partie.pack()

        else:
            reponse_color=color(mot_propo,mot_tempo,resultat_tempo)
            resultat=Label(text="Le résultat est: "+reponse_color)
            resultat.pack()
            indication=Label(text="Entrer un autre mot à l'aide des indications:")
            mot2=StringVar()
            mot2.set("")
            mot2=Entry(textvariable=mot2)
            mot_propo2=str(mot2.get())
            indication.pack()
            mot2.pack()
            
            def essai2():
                mot_propo2=mot2.get()
                gagne=False
                resultat_tempo=bien_place(mot_alea,mot_propo2)
                mot_tempo=cache_lettre(mot_alea,resultat_tempo)
                reponse=newresult(mot_propo2,mot_tempo,resultat_tempo)

                if reponse==mot_alea:
                    gagne=True
                    reponse_color=color(mot_propo2,mot_tempo,resultat_tempo)
                    resultat=Label(text="Le résultat est: "+reponse_color)
                    message=Label(text="Vous avez gagné !!!")
                    score_partie=Label(text="Votre score est de: 250 points.")
                    resultat.pack()
                    message.pack()
                    score_partie.pack()

                else:
                    reponse_color=color(mot_propo2,mot_tempo,resultat_tempo)
                    resultat=Label(text="Le résultat est: "+reponse_color)
                    resultat.pack()
                    indication=Label(text="Entrer un autre mot à l'aide des indications:")
                    mot3=StringVar()
                    mot3.set("")
                    mot3=Entry(textvariable=mot3)
                    mot_propo3=str(mot3.get())
                    indication.pack()
                    mot3.pack()

                    def essai3():
                        mot_propo3=mot3.get()
                        gagne=False
                        resultat_tempo=bien_place(mot_alea,mot_propo3)
                        mot_tempo=cache_lettre(mot_alea,resultat_tempo)
                        reponse=newresult(mot_propo3,mot_tempo,resultat_tempo)

                        if reponse==mot_alea:
                            gagne=True
                            reponse_color=color(mot_propo3,mot_tempo,resultat_tempo)
                            resultat=Label(text="Le résultat est: "+reponse_color)
                            message=Label(text="Vous avez gagné !!!")
                            score_partie=Label(text="Votre score est de: 200 points.")
                            resultat.pack()
                            message.pack()
                            score_partie.pack()

                        else:
                            reponse_color=color(mot_propo3,mot_tempo,resultat_tempo)
                            resultat=Label(text="Le résultat est: "+reponse_color)
                            resultat.pack()
                            indication=Label(text="Entrer un autre mot à l'aide des indications:")
                            mot4=StringVar()
                            mot4.set("")
                            mot4=Entry(textvariable=mot4)
                            mot_propo4=str(mot4.get())
                            indication.pack()
                            mot4.pack()

                            def essai4():
                                mot_propo4=mot4.get()
                                gagne=False
                                resultat_tempo=bien_place(mot_alea,mot_propo4)
                                mot_tempo=cache_lettre(mot_alea,resultat_tempo)
                                reponse=newresult(mot_propo4,mot_tempo,resultat_tempo)

                                if reponse==mot_alea:
                                    gagne=True
                                    reponse_color=color(mot_propo4,mot_tempo,resultat_tempo)
                                    resultat=Label(text="Le résultat est: "+reponse_color)
                                    message=Label(text="Vous avez gagné !!!")
                                    score_partie=Label(text="Votre score est de: 150 points.")
                                    resultat.pack()
                                    message.pack()
                                    score_partie.pack()

                                else:
                                    reponse_color=color(mot_propo4,mot_tempo,resultat_tempo)
                                    resultat=Label(text="Le résultat est: "+reponse_color)
                                    resultat.pack()
                                    indication=Label(text="Entrer un autre mot à l'aide des indications:")
                                    mot5=StringVar()
                                    mot5.set("")
                                    mot5=Entry(textvariable=mot5)
                                    mot_propo5=str(mot5.get())
                                    indication.pack()
                                    mot5.pack()

                                    def essai5():
                                        mot_propo5=mot5.get()
                                        gagne=False
                                        resultat_tempo=bien_place(mot_alea,mot_propo5)
                                        mot_tempo=cache_lettre(mot_alea,resultat_tempo)
                                        reponse=newresult(mot_propo5,mot_tempo,resultat_tempo)

                                        if reponse==mot_alea:
                                            gagne=True
                                            reponse_color=color(mot_propo5,mot_tempo,resultat_tempo)
                                            resultat=Label(text="Le résultat est: "+reponse_color)
                                            message=Label(text="Vous avez gagné !!!")
                                            score_partie=Label(text="Votre score est de: 100 points.")
                                            resultat.pack()
                                            message.pack()
                                            score_partie.pack()

                                        else:
                                            reponse_color=color(mot_propo5,mot_tempo,resultat_tempo)
                                            resultat=Label(text="Le résultat est: "+reponse_color)
                                            resultat.pack()
                                            indication=Label(text="Entrer un autre mot à l'aide des indications:")
                                            mot6=StringVar()
                                            mot6.set("")
                                            mot6=Entry(textvariable=mot6)
                                            mot_propo6=str(mot.get())
                                            indication.pack()
                                            mot6.pack()

                                            def essai6():
                                                mot_propo6=mot6.get()
                                                gagne=False
                                                resultat_tempo=bien_place(mot_alea,mot_propo6)
                                                mot_tempo=cache_lettre(mot_alea,resultat_tempo)
                                                reponse=newresult(mot_propo6,mot_tempo,resultat_tempo)

                                                if reponse==mot_alea:
                                                    gagne=True
                                                    reponse_color=color(mot_propo6,mot_tempo,resultat_tempo)
                                                    resultat=Label(text="Le résultat est: "+reponse_color)
                                                    message=Label(text="Vous avez gagné !!!")
                                                    score_partie=Label(text="Votre score est de: 50 points.")
                                                    resultat.pack()
                                                    message.pack()
                                                    score_partie.pack()

                                                else:
                                                    reponse_color=color(mot_propo6,mot_tempo,resultat_tempo)
                                                    resultat=Label(text="Le résultat est: "+reponse_color)
                                                    message=Label(text="Vous avez perdu. Le mot était: "+mot_alea)
                                                    score_partie=Label(text="Votre score est de: 0 points.")
                                                    resultat.pack()
                                                    message.pack()
                                                    score_partie.pack()

                                            bouton_done=Button(text="done",command=essai6)       
                                            bouton_done.pack()

                                    bouton_done=Button(text="done",command=essai5)       
                                    bouton_done.pack()

                            bouton_done=Button(text="done",command=essai4)       
                            bouton_done.pack()

                    bouton_done=Button(text="done",command=essai3)       
                    bouton_done.pack()

            bouton_done=Button(text="done",command=essai2)       
            bouton_done.pack()

    bouton_done=Button(text="done",command=essai1)       
    bouton_done.pack() 
