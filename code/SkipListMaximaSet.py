"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

from SkipListMap import SkipListMap
import random
import time

class SkipListMaximaSet():

    def __init__( self ):
        self._M = SkipListMap( -999999, 999999 )

    def best( self, x ):
        #return (X,Y) with cost <= c
        return self._M.find_le( x )

    def __str__( self ):
        return str( self._M )

    def add( self, x, y ):
        other = self._M.find_le( x )
        if ( other is not None ) and ( other[1] >= y ):
            return
        self._M[x] = y

        other = self._M.find_gt( x )
        while ( other is not None ) and ( other[1] <= y ):
            del self._M[other[0]]
            other = self._M.find_gt( x )

"""unit testing
"""
if __name__ == '__main__':

    print( "SkipListMaximaSet unit testing..." )

    M = SkipListMaximaSet()

    nb = 2000000
    random.seed( 131341 )

    avant = time.time()
    for i in range( nb ):
        x = random.randint( 15000, 200000 )
        y = random.randint(    80,    200 )
        M.add( x, y )
    apres = time.time()
    print( "Add", nb, "XY pairs in ", apres-avant, "seconds." )

    print( M )

    print( "End of testing." )
