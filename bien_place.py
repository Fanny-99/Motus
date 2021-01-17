def bien_place(mot,proposition):
    """
    Cette fonction prend en argument un mot donné et une proposition.
    Les lettres des arguments sont comparées.
    Si les lettres sont identiques, elle est ajoutée au résultat; Sinon, on ajoute au résultat un caractère "?".
    On retourne resultat.
    """
    
    resultat=""
    for i in range(len(mot)):
        if mot[i]==proposition[i]:
            resultat=resultat+mot[i]
        else:
            resultat=resultat+"?"
    return resultat