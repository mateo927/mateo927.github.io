import random
type matrice[T] = list[list[T]]
type chemin = list[int]

def init_pheromones(nb_sommets: int,tau_initial: float=1.0) -> matrice[float]:
    """Initialise la matrice des phéromones à tau_initial.     tau_initial est la contribution en phéromones de chaque arête"""
    traites=[[tau_initial] for _ in range (nb_sommets) for _ in range(nb_sommets)]
    for i in range(nb_sommets):
        traites[i][i]=0
    return traites


def calculer_visibilite(graphe: matrice[float]) -> matrice[float]:
    """Renvoie la matrice de visibilité.    La visibilité de chaque arête est l'inverse de la distance    """
    