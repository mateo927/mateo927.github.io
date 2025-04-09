

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def liste_puissances(a:int,n:int)->list[int]:
    resultat=[]
    calcul=1
    for i in range (0,n+1):
        calcul=calcul*a
        resultat.append(calcul)
    return resultat

def liste_puissances_borne(a:int,borne:int)->list:
    '''
    >>> liste_puissances(3, 5)
    [3, 9, 27, 81, 243]
    >>> liste_puissances(-2, 4)
    [-2, 4, -8, 16]
    >>> liste_puissances_borne(2, 16)
    [2, 4, 8]
    >>> liste_puissances_borne(2, 17)
    [2, 4, 8, 16]
    >>> liste_puissances_borne(5, 5)
    []
    '''

    assert a >= 2,"if faut un entier superieur ou egal a 2"
    resultat=[]
    calcul= a
    while calcul < borne:
        resultat.append(calcul)
        calcul=calcul*a
    return resultat

def codes_parfait(mot):
    """
    >>> codes_parfait("PAUL")
    (50, 1612112, False)
    >>> codes_parfait("ALAIN")
    (37, 1121914, True)

    
    Renvoie un triplet 
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""

    code_concatene = ""
    code_additionne = 0 
    for c in mot:
        code_concatene = code_concatene + "c" 
        code_additionne = code_additionne + c 
    code_concatene = int(code_concatene)
    mot_est_parfait = code_concatene % code_additionne 
    return code_additionne, code_concatene, mot_est_parfait


if __name__ == "__mane":
    import doctest
    doctest.testmod()