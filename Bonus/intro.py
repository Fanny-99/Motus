import time

print("Bonjour! Souhaitez-vous visionner l'introduction ?\nRépondez par oui ou par non.")
reponse=input()

if reponse=="oui": 
    print("Bienvenue Joueur/Joueuse!")
    time.sleep(3)
    print("... Hmmmm peut-être un peu trop formel comme message de salutations.")
    time.sleep(3)
    print("Je me présente, je suis Motus, un jeu qui reprend le même principe que celui de l'émission télé.")
    time.sleep(3)
    print("Si si, vous savez! Le jeu télé qui était présenté par Thierry Beccaro!")
    time.sleep(3)
    print("Vous ne le connaissez pas?")
    time.sleep(3)
    print("Moi non plus.")
    time.sleep(3)
    print("Bref! Maintenant que je me suis présenté, c'est à votre tour!")
    time.sleep(3)
    print("Comment vous appelez-vous donc, cher Joueur/Joueuse ?")
    print("Votre Nom : ")

    nom = input()

    print ("Ravi de faire votre connaissance, " , nom, "!")
    time.sleep(3)
    print("A présent, si nous commencions à jouer?")
    time.sleep(3)
    print ("Nous allons faire ensemble 5 parties successives de Motus.")
    time.sleep(3)
    print("A chaque fois, vous pourrez choisir votre niveau de difficulté, et vous disposerez de 6 essais pour chaque mot à trouver.")
    time.sleep(3)
    print("En fonction du nombre d'essais qu'il vous aura fallu pour trouver le mot et de la difficulté, vous vous verrez attribuer un score.")
    time.sleep(3)
    print ("Chaque score obtenu augmentera votre score total.")
    time.sleep(3)
    print("Attention toutefois à ne pas viser trop haut si vous voulez marquer des points!")
    time.sleep(3)

else:
    print("Veuillez entrer votre nom s'il vous plaît:")
    nom=input()
    print("Amusez-vous bien",nom,"!")
    time.sleep(2)