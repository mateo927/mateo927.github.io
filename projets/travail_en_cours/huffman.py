from structures.hierarchiques import arbrebin_mutable as ab
from structures.hierarchiques import dessin
def get_dicofreq(texte: str) -> dict[str, int]:
    """Renvoie un dictionnaire de fréquence des lettres du texte en entrée"""
    d=dict()
    for i in texte:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    return d 



def get_arbre_huffman(dicofreq: dict[str, int]) -> ab.Noeud:
    """Renvoie un arbre de Huffman d'après le dictionnaire de fréquences des lettres"""
    # Etape 1: Construire EN COMPREHENSION une liste de feuilles d'après le dictionnaire de fréquences
    lst=[ab.Noeud((i,dict[i]),ab.ARBRE_VIDE,ab.ARBRE_VIDE) for i in dicofreq]
    # Etape 2: Construire l'arbre de Huffman en agrégeant progresivement les arbres de la liste
    lst=lst.sort(key=x : [])
    
    
    return lst
test=get_arbre_huffman({'a': 3, 'b': 2, 'c': 1, 'z': 1, 'e': 1, 'r': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1})
print(test) 


def get_codes(arbre: ab.Noeud) -> dict[str, str]:
    """
    Fonction récursive.
    Renvoie un dictionnaire contenant la codification binaire de chaque caractère
    """
    pass

def compresser(texte, codes: dict[str, str]) -> str:
    """Compresse un texte en utilisant le dictionnaire d'encodage"""
    pass

def decompresser(texte, codes: dict[str, str]) -> str:
    """Décompresse un texte en utilisant le dictionnaire d'encodage"""
    pass
#uv run -m projets.huffman