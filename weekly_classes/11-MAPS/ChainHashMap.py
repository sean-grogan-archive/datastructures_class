"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

from HashMap import HashMap
from UnsortedListMap import UnsortedListMap
import random
import time

class ChainHashMap( HashMap ):

    def _bucket_getitem( self, j, k ):
        bucket = self._T[j]
        if bucket is None:
            return False
        return bucket[k]

    def _bucket_setitem( self, j, k, v ):
        if self._T[j] is None:
            self._T[j] = UnsortedListMap()
        oldsize = len( self._T[j] )
        self._T[j][k] = v
        if len( self._T[j] ) > oldsize:
            self._n += 1

    def _bucket_delitem( self, j, k ):
        bucket = self._T[j]
        if bucket is None:
            return False
        del bucket[k]

    def __iter__( self ):
        for bucket in self._T:
            if bucket is not None:
                for key in bucket:
                    yield key


"""unit testing
"""
if __name__ == '__main__':

    print( "ChainHashMap unit testing..." )

    M = ChainHashMap()

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

