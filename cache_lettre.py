def cache_lettre(mot,resultat):
    """
    Cette fonction prend en argument un mot et un résultat.
    Elle crée une copie de mot dans laquelle 
    les lettres bien placées de resultat sont remplacées par # et les autres sont remplacées par ?
    On retourne la copie mot1.
    """
    mot1=""
    for i in range(len(mot)):
        if resultat[i]=="?":
           mot1=mot1+mot[i]
        else:
            mot1=mot1+"#"
    return mot1
