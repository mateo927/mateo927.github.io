from random import randint

def lancer(n:int)->list:
    tab=[]
    for _ in range (n):
        tab.append(randint(1,6))
    return tab

def paire_6(tab:list[int])->bool:
    '''
    >>> lancer1 = lancer(5)
    >>> lancer1
    [5, 6, 6, 2, 2]
    >>> paire_6(lancer1)
    True
    >>> lancer2 = lancer(5)
    >>> lancer2
    [6, 5, 1, 6, 6]
    >>> paire_6(lancer2)
    True
    >>> lancer3 = lancer(3)
    >>> lancer3
    [2, 2, 6]
    >>> paire_6(lancer3)
    False
    >>> lancer4 = lancer(0)
    >>> lancer4
    []
    >>> paire_6(lancer4)
    False
    '''
    compte_6=["y a un 6" for i in tab if i==6]
    return len(compte_6)

    


def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            nouvelle_image[i][j] = 255 - image[i][j] 
    return nouvelle_image
    
def binaire(image, seuil):
    '''
    >>> img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],
    [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
    >>> nombre_lignes(img)
    4
    >>> nombre_colonnes(img)
    5
    >>> negatif(img)
    [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186],
    [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
    >>> binaire(img,120)
    [[0, 0, 255, 255, 0],[0, 255, 255, 255, 0],
    [255, 255, 255, 0, 0],[255, 0, 0, 255, 255]]

    
    
    renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 255 sinon'''
    
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            if image[i][j] < seuil : 
                nouvelle_image[i][j] = 0 
            else:
                nouvelle_image[i][j] = 255 
    return nouvelle_image



if __name__ == "__mane__":
    import doctest
    doctest.testmod()
