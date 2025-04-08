

def correspond(mot:str,mot_a_trous:str)->bool:
    '''
    >>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
    True
    >>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
    False
    >>> correspond('STOP', 'S*')
    False
    >>> correspond('AUTO', '*UT*')
    True
    '''
    i = 0
    for lettre in mot_a_trous:
        if lettre == "*":
            i += 1
        elif i < len(mot) and lettre != mot[i]:
            return False
        else:
            i += 1
    return i == len(mot)





def est_cyclique(plan):
    '''
    >>> est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})
    False
    >>> est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})
    True
    >>> est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})
    True
    >>> est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})
    False

    Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.
    '''
    expediteur = 'A'
    destinataire = plan['A'] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire] 
        nb_destinataires = nb_destinataires+1

    return nb_destinataires == len(plan)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    