"""Classe pour le cours IFT2015
   Écrit par Francois Major le 12 janvier 2014.

   Cette classe définit un intervalle, soit
   l'équivalent du "range" en python.

   Comportement :
     range( inf )           = 0, 1, ... stop-1
     range( inf, sup )      = inf, inf+1, ... sup-1
     range( inf, sup, inc ) = inf, inf+inc, inf+2*inc, ...
"""

class intervalle:

    """Un intervalle se définit par:
       - une valeur inf
       - une valeur sup
       - une valeur inc (increment)
    """

    """Constructeur
    """
    def __init__( self, inf, sup = None, inc = 1 ):

        if inc == 0:
            raise ValueError( "L'incrément ne peut pas être 0" )

        if sup is None: #cas range( sup )
            inf, sup = 0, inf

        self._length = max( 0, ( sup - inf + inc - 1 ) // inc )

        self._inf = inf
        self._sup = sup
        self._inc = inc
        
    """Les methodes
    """

    """__str__ retourne une chaîne lisible
    """
    def __str__( self ):
        return "intervalle( " + str( self._inf ) + ", " + str( self._sup ) + ", " + str( self._inc ) + " )"

    """__len__ retourne le nombre d'éléments dans l'intervalle
    """
    def __len__( self ):
        return self._length

    """__getitem__ retourne le kème élément de l'intervalle
    """
    def __getitem__( self, k ):
        # si k < 0, index à partir de la fin de l'intervalle
        if k < 0:
            k += len( self )

        # si k indice un élément en dehors de l'intervalle,
        # alors il faut lancer une exception.
        if not 0 <= k < self._length:
            raise IndexError( 'index hors limite' )

        # calculer et retourne le kè élément
        return self._inf + k * self._inc

    """Avec __len__ et __getitem__ la classe
       devient automatiquement itérable.
    """

"""Fin class intervalle:
"""

"""Validation de la classe (unit testing)
"""

if __name__ == '__main__':

    int1 = intervalle( 10 )
    print( int1 )

    int2 = intervalle( 0, 10 )
    print( int2 )

    int3 = intervalle( 0, 10, 2 )
    print( int3 )

    for i in int3:
        print( i )

    int4 = intervalle( -10, 10, 2 )
    print( int4 )

    for i in int4:
        print( i )

"""Fin Validation de la classe (unit testing)
"""
