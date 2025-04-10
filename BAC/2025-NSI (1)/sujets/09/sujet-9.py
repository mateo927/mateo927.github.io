
def multiplication(n1:int,n2:int)->int:
    '''
    >>> multiplication(3, 5)
    15
    >>> multiplication(-4, -8)
    32
    >>> multiplication(-2, 6)
    -12
    >>> multiplication(-2, 0)
    0
    '''
    
    
    original_n1=0
    if n1==0 or n2==0:
        return 0
    
    elif n1==0 and n2==0:
        return 0
    
    elif n1 <0 and n2<0:
        n1=-n1
        n2=-n2
        original_n1=n1
        for _ in range (n2):
            n1=n1+original_n1
        return n1
    
    elif n1<0 and n2>0:
        n1=-n1
        n2=-n2
        original_n1=n1
        for _ in range(n2):
            n1=n1-original_n1
        return n1
    else:
        original_n1=n1
        for _ in range(n2):
            n1=n1+original_n1
        return n1





def dichotomie(tab, x):
    """
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
    True
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)
    False


    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = 0
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1 
    return False 


if __name__ == "__main__":
    import doctest
    doctest.testmod()