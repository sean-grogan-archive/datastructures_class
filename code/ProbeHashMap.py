"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

from HashMap import HashMap
import random
import time

class ProbeHashMap( HashMap ):

    _AVAIL = object()

    def _is_available( self, j ):
        return self._T[j] is None or self._T[j] is ProbeHashMap._AVAIL

    def _find_slot( self, j, k ):
        firstAvail = None
        while True:
            if self._is_available( j ):
                if firstAvail is None:
                    firstAvail = j
                if self._T[j] is None:
                    return (False,firstAvail)
            elif k == self._T[j]._key:
                return (True,j)
            j = (j + 1) % len( self._T )

    def _bucket_getitem( self, j, k ):
        found, s = self._find_slot( j, k )
        if not found:
            return False
        return self._T[s]._value

    def _bucket_setitem( self, j, k, v ):
        found, s = self._find_slot( j, k )
        if not found:
            self._T[s] = self._Item( k, v )
            self._n += 1
        else:
            self._T[s]._value = v

    def _bucket_delitem( self, j, k ):
        found, s = self._find_slot( j, k )
        if not found:
            return False
        self._T[s] = ProbeHashMap._AVAIL

    def __iter__( self ):
        for j in range( len( self._T ) ):
            if not self._is_available( j ):
                yield self._T[j]._key


"""unit testing
"""
if __name__ == '__main__':

    print( "ProbeHashMap unit testing..." )

    M = ProbeHashMap()

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

