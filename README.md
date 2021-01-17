# Motus

--But et règles du jeu:

Motus est un jeu où le but est de deviner un mot caché. 
Pour cela, le joueur est invité à choisir un niveau qui détermine la longueur du mot à deviner (entre 1 et 25 lettres). Après avoir entré le niveau souhaité, le jeu propose de découvrir à mot à partir de la première et de la longueur de ce mot. Le joueur a 6 essais pour le trouver. A chaque essai, le mot donner par le joueur apparait avec un code couleur: -bleu: la lettre écrite est la bonne / -rouge: la lettre écrite n'est pas la bonne.
Si le joueur arrive à trouver le mot en moins de 6 essais, la partie s'arrête et un score lui ai attribué en fonction du nombre d'essai qu'il lui a fallu pour trouver la solution (entre 300 et 50 points). Si au contraire il ne trouve pas le mots, la partie s'arrête, le mot caché est donné et le joueur se voit attribué 0 point.
Une partie complète se déroule en 5 manches entre lesquelles le joueur pourra changer de niveau. Au terme de ces 5 parties, une score final est calculé en sommant les scores de l'ensemble des parties réalisées.


--Lancement du jeu et interactions:

Pour lancer le jeu, il faut tout d'abord télécharger tous les fichiers fournis. La première fois que le jeu est lancé, il faut décommenter la partie commentée avec le tableau à la fin du code principal. Cela permet de créer le fichier où seront sauvegardés les scores. Il est nécessaire de commenter cette partie à la fin de la première partie de jeu, sinon le tableau sera réinitialisé à chaque fois. Pour lancer le jeu, il faut entrer la commande suivante dans le terminal:python motus.py.

Après avoir entré la commande, le jeu va vous proposer de suivre ou non une introduction au jeu dans laquelle se trouve le but et les règles de ce dernier. Il faut alors écrire oui ou non. Il sera demandé au joueur d'entrer son nom. Il servira lors de son inscription dans le tableau des scores s'il fait parti du top 10.
Une fois l'introduction passée, le joueur doit écrire le niveau qu'il souhaite pour la première manche. Il doit par la suite écrire le mot qu'il souhaite soumettre. A la fin de la manche il lui sera à nouceau demandé de choisir un niveau et ainsi de suite...


--Organigramme:

Voir organigramme



--Rôle des fonctions:

-motus: code principal (ce n'est pas une fonction) qui permet le déroulement du jeu et l'enregistrement des scores.

-bien_place:fonction qui compare le mot proposé par le joueur à celui qu'il doit trouver. Elle crée et renvoie une chaîne de caractère en ne conservant que les lettres bien placées et en remplaçant les autres par ? .

-cache_lettre: fonction assez similaire à la précédente. Elle crée une copie du mot proposé par le joueur dans laquelle les lettres bien placées de la proposition sont remplacées par # et les autres sont remplacées par ?.

-recherche:fonction qui cherche la présence d'un caractère précis dans le mot proposé par le joueur. Elle renvoie l'indice de la première occurence de ce caractère ou -1 s'il n'est pas présent dans le mot. 

-remplace: fonction qui crée une copie du mot donné par le joueur et dont le caractère d'indice ind est remplacé par le caractère trouvé avec la fonction recherche.

-newresult: fonction qui crée et renvoie une copie du mot proposé par le joueur sur laquelle ont fera les différents tests et les modifications dans la suite du code du jeu. A partir du résultat de bien_place, si un caractère a été remplacé par ?, on va chercher l'indice de ce caractère avec la fonction recherche. Si cette dernière retourne un indice différent de -1, alors on ajoute à la liste qui sert de copie le caractère proposé dans recherche et on remplace le caractère du mot provenant de cache_lettre par #. Sinon on ajoute juste à la liste le caractère proposé dans recherche. Si, dans le résultat de bien_place, le caractère n'a pas été remplacé par ?, alors on ajoute à la liste le caractère proposé dans bien_place.

-niveau: fonction qui va chercher un mot aléatoirement dans une liste donnée en fonction du niveau choisi par le joueur et le retourne.Ce mot sera celui que le joueur devra deviner. Pour cela, le joueur va choisir un niveau entre novice/facile/moyen/difficile/expert qui va définir une fourchette de tailles pour le mot. Par la suite, la fonction va parcourir aléatoirement la liste de mot donnée dans un fichier jusqu'à trouver un mot ayant les caractéristiques voulues.

-color:fonction qui colore en bleu les lettres bien placées et en rouge les lettres mal placées. Le code est la même que celui de newresult, sauf qu'il possède en plus la possibilité de donner des couleurs aux lettres.


-intro: première partie du code (séparée du code principal) (ce n'est pas une fonction) qui permet au joueur de choisir entre avoir une présentation du jeu et de son fonctionnement ou seulement un rappel des niveaux avant de commencer à jouer.
