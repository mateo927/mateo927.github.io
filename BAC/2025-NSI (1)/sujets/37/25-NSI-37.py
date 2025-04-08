def gb_vers_entier(tab:list[bool])->int:
    '''
    >>> gb_vers_entier([])
    0
    >>> gb_vers_entier([True])
    1
    >>> gb_vers_entier([True, False, True,False, False, True, True])
    83
    >>> gb_vers_entier([True, False, False, False,False, False, True, False])
    130
    '''

    nombre_ele= len(tab)
    resultat=0
    for booleen in range (nombre_ele):
        if tab[booleen]==True:
            resultat+=2**(nombre_ele-(booleen+1))
    return resultat



def tri_insertion(tab):
    '''
    >>> tab = [98, 12, 104, 23, 131, 9]
    >>> tri_insertion(tab)
    >>> tab
    [9, 12, 23, 98, 104, 131]

    Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i] 
        # la variable j sert à déterminer 
        # où placer la valeur à ranger
        j = i - 1
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j >= 0 and valeur_insertion < tab[j]: 
            tab[j + 1] = tab[j]
            j = j - 1  # Correction: decrement j instead of increment
        tab[j + 1] = valeur_insertion


if __name__ == "__main__":
    import doctest
    doctest.testmod()