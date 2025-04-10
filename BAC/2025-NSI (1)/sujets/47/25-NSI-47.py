type arbre_bin = dict[str,list[int]] | None

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

def taille (arb:arbre_bin,lettre:str)->int:   
    '''
    >>> taille(a, 'F')
    9
    >>> taille(a, 'B')
    5
    >>> taille(a, 'I')
    2
    '''
    if arb[lettre][0] ==  "" and arb[lettre][1] ==  "":
        return 1
    elif arb[lettre][0] ==  "":
        return 1 +taille(arb,arb[lettre][1])
    
    elif arb[lettre][1] ==  "":
        return 1 +taille(arb,arb[lettre][0])
    
    return 1 + taille(arb,arb[lettre][0])+taille(arb,arb[lettre][1])


def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_selection(tab):
    '''
    >>> tab = [41, 55, 21, 18, 12, 6, 25]
    >>> tri_selection(tab)
    >>> tab
    [6, 12, 18, 21, 25, 41, 55]
    
    Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N): 
        imin = k
        for i in range(k + 1, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin)


if __name__ == "__main__":
    import doctest
    doctest.testmod()