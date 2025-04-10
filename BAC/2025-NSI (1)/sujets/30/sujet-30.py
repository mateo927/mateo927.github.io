def delta(tab:list)->list:
    '''
    >>> delta([1000, 800, 802, 1000, 1003])
    [1000, -200, 2, 198, 3]
    >>> delta([42])
    [42]
    '''
    nouveau_tableau=[]
    for i in range (len(tab)):
        if i==0:
            nouveau_tableau.append(tab[i])
        else:
            nouveau_tableau.append((tab[i]-tab[i-1]))
    return nouveau_tableau

    



class Expr:
    
    """
    >>> a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))
    >>> a.infixe()
    '(1+2)'
    >>> b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)),'*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None)))
    >>> b.infixe()
    '((1+2)*(3+4))'
    >>> e = Expr(Expr(Expr(None, 3, None), '*', Expr(Expr(None, 8, None),'+', Expr(None, 7, None))),'-', Expr(Expr(None, 2, None), '+', Expr(None, 1, None)))
    >>> e.infixe()
    '((3*(8+7))-(2+1))'

    Classe implémentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérateur ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = ""
        if self.gauche is not None:
            s = s + '(' + self.gauche.infixe() 
        s = s + str(self.valeur) 
        if self.droite is not None: 
            s = s + self.droite.infixe() + ')' 
        return s


if __name__ =="__main__":
    import doctest
    doctest.testmod()