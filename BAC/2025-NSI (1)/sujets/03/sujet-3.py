def fibonacci(n:int)->int:
    '''
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(25)
    75025
    '''
    suite=[1,1]
    for x in range(n-2):
        suite.append(suite[x]+suite[x+1])
    return suite[-1]


def eleves_du_mois(eleves, notes):
    '''
    >>> eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
    >>> notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
    >>> eleves_du_mois(eleves_nsi, notes_nsi)
    (80, ['c', 'f', 'h'])
    '''
    note_maxi = 0
    meilleurs_eleves = [] 

    for i in range(len(eleves)): 
        if notes[i] == note_maxi: 
            meilleurs_eleves.append(eleves[i]) 
        elif notes[i] > note_maxi:
            note_maxi = notes[i] 
            meilleurs_eleves = [eleves[i]] 

    return (note_maxi, meilleurs_eleves)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    