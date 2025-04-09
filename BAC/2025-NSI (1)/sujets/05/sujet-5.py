def renverse(mot:str)->str:
    '''>>> renverse("")
    ''
    >>> renverse("abc")
    'cba'
    >>> renverse("informatique")
    'euqitamrofni'
    '''

    nouveau_mot=""
    nombre_lettre=len(mot)
    for lettre in mot:
        nouveau_mot = nouveau_mot + mot[nombre_lettre-1]
        nombre_lettre-=1
    return nouveau_mot


def crible(n):
    """
    >>> crible(40)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    >>> crible(5)
    [2, 3]
    
    Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i) 
            multiple = i * 2
            while multiple < n:
                tab[multiple] = False
                multiple += i
    return premiers


if __name__ == "__main__":
    import doctest
    doctest.testmod()
