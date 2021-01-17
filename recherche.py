def recherche(mot,caract):
    """
    Cette fonction prend en argument un mot et un caractère caract.
    Elle cherche la présence d'un caractère précis dans mot.
    Elle retourne l'indice i de la première occurence de caract ou -1 s'il n'est pas présent dans le mot.
    """
    for i in range(len(mot)):
        if mot[i]==caract:
            return i
        else:
            return (-1)