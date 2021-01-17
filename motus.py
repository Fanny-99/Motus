from bien_place import bien_place
from cache_lettre import cache_lettre
from newresult import newresult
from niveau import niveau
from couleur import color
import intro
import csv
import time

intro
nom=intro.nom

score=0
nb_partie=0

print("Les différents niveaux sont:")
time.sleep(2)
print("-novice (mot de 1 à 5 lettres)")
time.sleep(2)
print("-facile (mot de 6 à 10 lettres)")
time.sleep(2)
print("-moyen (mot de 11 à 15 lettres)")
time.sleep(2)
print("-difficile (mot de 16 à 20 lettres)")
time.sleep(2)
print("-expert (mot de 21 à 25 lettres)")
time.sleep(2)

for nb_partie in range (5):
    print("Choisissez un niveau:")
    niveau_choisi=input()

    mot_alea=niveau(niveau_choisi)
    taille=len(mot_alea)
    premiere_lettre=mot_alea[0]
    print("Entrer un mot de",taille,"lettres dont la première est",premiere_lettre,":")
    mot=input()


    compteur=0
    score_partie=300
    gagne=False
    liste_result=[]


    while compteur<=5 and gagne==False:
        print(compteur)
        
        print(mot_alea)
        

        resultat_tempo=bien_place(mot_alea,mot)
        mot_tempo=cache_lettre(mot_alea,resultat_tempo)
        reponse=newresult(mot,mot_tempo,resultat_tempo)

        if reponse==mot_alea:
            gagne=True
            reponse_color=color(mot,mot_tempo,resultat_tempo)
            print("Le résultat est:",reponse_color)
            break
        else:
            
            compteur+=1
            print(compteur)
            reponse_color=color(mot,mot_tempo,resultat_tempo)
            print("Le résultat est:",reponse_color)
            liste_result.append(mot)
            print(liste_result)
            if compteur<6:
                print("Entrer un autre mot à l'aide des indications:")
                mot=input()
            else:
                break
            

    print(gagne) 
   
    if compteur==0 and gagne==True:
        score_partie=300
    elif compteur==1 and gagne==True:
        score_partie=250
    elif compteur==2 and gagne==True:
        score_partie=200
    elif compteur==3 and gagne==True:
        score_partie=150
    elif compteur==4 and gagne==True:
        score_partie=100
    elif compteur==5 and gagne==True:
        score_partie=50
    else:
        score_partie=0

    if gagne==True:
        print("Vous avez gagné !!!")
        print("Votre score est de :",score_partie,"points")
    else:
        print("Vous avez perdu. Le mot était:",mot_alea)
        print("Votre score est de :",score_partie,"points")

    score+=score_partie



print("Votre score final est de :", score,"points !")



# tableau=[["Tableau des scores"],["Classement","Nom","Score"],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[8,0,0],[9,0,0],[10,0,0]]


# with open ("score.csv", "w") as f:
#     write=csv.writer(f,delimiter=";")
#     write.writerows(tableau)



with open ("score.csv","r") as f:

    table=[]
    liste_score=[]
    liste_nom=[]
    read=csv.reader(f,delimiter=";")
    for row in read:
        table.append(row)
    for i in range (4,24,2):
        liste_score.append(int(table[i][2]))
        liste_nom.append(table[i][1])

    for i in range (0,10):            
        if liste_score[i]<=score:
            liste_score.append(score)
            liste_score.sort()
            liste_score.remove(liste_score[0])
            
            l=len(liste_nom)-1
            while l >i :
                liste_nom[l]=liste_nom[l-1]
                l-=1
            
            liste_nom[i]=nom


            j=4
            for k in range (0,10):
                table[j][2]=liste_score[9-k]
                table[j][1]=liste_nom[k]
                j+=2

            print("Nouveau Record!!!")
            break


with open ("score.csv","w",newline="") as f:

    write=csv.writer(f,delimiter=";")
    write.writerows(table)