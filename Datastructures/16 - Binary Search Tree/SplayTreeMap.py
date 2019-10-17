"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 11 avril 2014.
   Ref: Data Structure & Algorithms in Python
        Goodrich, Tamassia et Goldwasser, 2013
"""
import random
import time
from TreeMap import TreeMap

class SplayTreeMap( TreeMap ):

    def _splay( self, p ):
        while p != self.root():
            parent = self.parent( p )
            grand = self.parent( parent )
            if grand is None:
                #zig case
                self._rotate( p )
            elif ( parent == self.left( grand ) ) == ( p == self.left( parent ) ):
                #zig-zig case
                self._rotate( parent )
                self._rotate( p )
            else:
                #zig-zag case
                self._rotate( p )
                self._rotate( p )

    def _rebalance_insert( self, p ):
        self._splay( p )

    def _rebalance_delete( self, p ):
        if p is not None:
            self._splay( p )

    def _rebalance_access( self, p ):
        self._splay( p )

"""unit testing
"""
if __name__ == '__main__':

    print( "SplayTreeMap unit testing..." )

    M = SplayTreeMap( )
    nb = 100000
    random.seed( 131341 )

    #Insertion
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        M[key] = key
    apres = time.time()
    print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )

    #Access
    random.seed( 131341 )
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        x = M[key]
    apres = time.time()
    print( "Access of", nb, "keys in ", apres-avant, "seconds." )

    #Delete
    avant = time.time()
    nbdel = 0
    for i in range( nb ):
        key = random.randint( 0, nb )
        del M[key]
    apres = time.time()
    print( "Delete ", nb, "keys in ", apres-avant, "seconds." )

#     M = SplayTreeMap( )
#     print( len( M ) ) #0
#     M['K'] = 2
#     print( M )
#     print( len( M ) )
#     M['B'] = 4
#     print( M )
#     print( len( M ) )
#     M['U'] = 2
#     print( M )
#     print( len( M ) )
#     M['V'] = 8
#     print( M )
#     print( len( M ) )

#     M['K'] = 9
#     print( M )
#     print( len( M ) )
#     print( M['B'] )
#     print( M['X'] )
#     print( M.get( 'F' ) )
#     print( M.get( 'F', 5 ) )
#     print( M.get( 'K', 5 ) )
#     print( M )
#     print( len( M ) )
#     del M['V']
#     print( "pop(K) = ", M.pop( 'K' ) )
#     print( M )
#     for key in M.keys():
#         print( str( key ) )
#     for value in M.values():
#         print( str( value ) )
#     for item in M.items():
#         print( str( item ) )
#     print( M.setdefault( 'B', 1 ) )
#     print( M.setdefault( 'AA', 1 ) )
#     print( M )
#     print( M.popitem() )
#     print( M )
#     print( M.find_min() )
#     print( M.find_max() )

#     M = SplayTreeMap()
#     nb = 50
#     random.seed( 131341 )
#     avant = time.time()
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         M[key] = key
#     apres = time.time()
#     print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )
#     print( M )

#     print( M.find_min() )
#     print( M.find_max() )

#     print( M.find_ge( 25 ) )
#     print( M.find_gt( 25 ) )
#     print( M.find_le( 25 ) )
#     print( M.find_lt( 25 ) )
#     print( M.find_lt( 0 ) )

#     for (x,y) in M.find_range( 12, 100 ):
#         print( "x =", x, ", y =", y )
    
    print( "End of testing." )

