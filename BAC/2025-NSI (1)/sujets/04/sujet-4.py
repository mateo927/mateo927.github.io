def ecriture_binaire_entier_positif(n: int) -> str:
    '''
    >>> ecriture_binaire_entier_positif(0)
    '0'
    >>> ecriture_binaire_entier_positif(2)
    '10'
    >>> ecriture_binaire_entier_positif(105)
    '1101001'
    '''
    if n == 0:
        return '0'
    binaire = ""
    while n > 0:
        binaire = str(n % 2) + binaire
        n = n // 2
    return binaire



def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] =tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''
    >>> tab = []
    >>> tri_bulles(tab)
    >>> tab
    []
    >>> tab2 = [9, 3, 7, 2, 3, 1, 6]
    >>> tri_bulles(tab2)
    >>> tab2
    [1, 2, 3, 3, 6, 7, 9]
    >>> tab3 = [9, 7, 4, 3]
    >>> tri_bulles(tab3)
    >>> tab3
    [3, 4, 7, 9]
    
    Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n): 
        for j in range(i): 
            if tab[j] > tab[i]: 
                echange(tab, j, i) 


if __name__ == "__main__":
    import doctest
    doctest.testmod()