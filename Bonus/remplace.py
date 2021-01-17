def remplace(mot,ind,caract):
    """
    Cette fonction prend en argument un mot, un indice ind et un caractère caract.
    Elle crée une copie de mot et le caractère d'indice ind de mot y est remplacé par caract.
    Elle retourne la copie new.
    """
    new=""
    for i in range(len(mot)):
        if i==ind:
            new=new+caract
        else:
            new=new+mot[i]
    return new