type tab = list 
def max_et_indice(tab:tab)->tuple:
    '''
    >>> max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
    (9, 3)
    >>> max_et_indice([-2])
    (-2, 0)
    >>> max_et_indice([-1, -1, 3, 3, 3])
    (3, 2)
    >>> max_et_indice([1, 1, 1, 1])
    (1, 0)
    '''
    max = 0
    indice_max=0
    for v in range(len(tab)):  
        if tab[v] > max:
            max = tab[v]
            indice_max = v
    return max, indice_max 
        





def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = []

    for x in tab:
        if x < 1 or x >n or x in vus: 
            return False
        vus.append(x) 
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    >>> est_un_ordre([1, 6, 2, 8, 3, 7])
    False
    >>> est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9])
    True
    >>> nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9])
    4
    >>> nombre_points_rupture([1, 2, 3, 4, 5])
    0
    >>> nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5])
    7
    >>> nombre_points_rupture([2, 1, 3, 4])
    2
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre),'c est pas un ordre' 
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < n: 
        if ordre[i]-ordre[i+1] not in [-1, 1]: # l'écart n'est pas 1 
            nb = nb + 1
        i = i + 1
    if ordre[i] != n: # le dernier n'est pas n 
        nb = nb + 1
    return nb


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    