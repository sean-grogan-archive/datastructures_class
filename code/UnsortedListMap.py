"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

from Map import Map
import random
import time

class UnsortedListMap( Map ):

    def __init__( self ):
        self._T = []

    def __getitem__( self, k ):
        for item in self._T:
            if k == item._key:
                return item._value
        return False

    def __setitem__( self, k, v ):
        for item in self._T:
            if k == item._key:
                item._value = v
                return
        #no match
        self._T.append( self._Item( k, v ) )

    def __delitem__( self, k ):
        for j in range( len( self._T ) ):
            if k == self._T[j]._key:
                self._T.pop( j )
                return
        return False

    def __len__( self ):
        return len( self._T )

    def __iter__( self ):
        for item in self._T:
            yield item._key

    def __contains__( self, k ):
        return self[k]

"""unit testing
"""
if __name__ == '__main__':

    print( "UnsortedListMap unit testing..." )

    M = UnsortedListMap()

    nb = 50000
    random.seed( 131341 )
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        M[key] = key
    apres = time.time()
    print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )

    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        M.get( key )
    apres = time.time()
    print( "Access to", nb, "keys in ", apres-avant, "seconds." )

#     print( len( M ) ) #0
#     M['K'] = 2
#     M['B'] = 4
#     M['U'] = 2
#     M['V'] = 8
#     M['K'] = 9
#     print( M['B'] )
#     print( M['X'] )
#     print( M.get( 'F' ) )
#     print( M.get( 'F', 5 ) )
#     print( M.get( 'K', 5 ) )
#     print( len( M ) )
#     del M['V']
#     print( M.pop( 'K' ) )
#     for key in M.keys():
#         print( str( key ) )
#     for value in M.values():
#         print( str( value ) )
#     for item in M.items():
#         print( str( item ) )
#     print( M.setdefault( 'B', 1 ) )
#     print( M.setdefault( 'A', 1 ) )
#     print( M )
#     print( M.popitem() )
    

    print( "End of testing." )

