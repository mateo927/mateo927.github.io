
from calendar import c


type liste_adjacente = list[list[int]]
type graphe = liste_adjacente
def voisins_entrants(adj:graphe, x:int)->list[int]:
    '''Renvoie la liste des voisins entrants de x dans le graphe adj.'''
    voisins = []
    for i in range(len(adj)):
        if x in adj[i]:
            voisins.append(i)
    return voisins
exemple = [[1, 2], [2], [0], [0]]
print(voisins_entrants(exemple, 0))

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.
    >>> nombre_suivant('1211')
    '111221'
    >>> nombre_suivant('311')
    '1321'
    '''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += compte + chiffre
            chiffre = s[i] 
            compte = 1
    lecture_chiffre = compte + chiffre
    resultat += lecture_chiffre
    return resultat



