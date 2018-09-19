"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 30 mars 2014.
   Ref: Data Structure & Algorithms in Python
        Goodrich, Tamassia et Goldwasser, 2013
"""
import random
import time
from TreeMap import TreeMap

class AVLTreeMap( TreeMap ):

    class _Node( TreeMap._Node ):
        __slots__ = '_height' #additional member

        def __init__( self, element, parent = None, left = None, right = None ):
            super().__init__( element, parent, left, right )
            self._height = 0

        def left_height( self ):
            return self._left._height if self._left is not None else 0

        def right_height( self ):
            return self._right._height if self._right is not None else 0

    def __str__( self ):
        pp = super().__str__()
        pp += "(h = " + str( self.root()._node._height ) + ")"
        return pp

    def _recompute_height( self, p ):
        p._node._height = 1 + max( p._node.left_height(), p._node.right_height() )
        
    def _isbalanced( self, p ):
        return abs( p._node.left_height() - p._node.right_height() ) <= 1

    def _tall_child( self, p, favorleft = False ):
        if p._node.left_height() + ( 1 if favorleft else 0 ) > p._node.right_height():
            return self.left( p )
        else:
            return self.right( p )

    def _tall_grandchild( self, p ):
        child = self._tall_child( p )
        #if child is on left, favor left grandchild; else favor right grandchild
        alignment = ( child == self.left( p ) )
        return self._tall_child( child, alignment )

    def _rebalance( self, p ):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced( p ):
                #perform trinode restructuring, setting p to resulting root,
                #and recompute new local heights after the restructuring
                p = self._restructure( self._tall_grandchild( p ) )
                self._recompute_height( self.left( p ) )
                self._recompute_height( self.right( p ) )
            self._recompute_height( p )
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent( p )

    def _rebalance_access( self, p ):
        self._rebalance( p )

    def _rebalance_delete( self, p ):
        self._rebalance( p )

"""unit testing
"""
if __name__ == '__main__':

    print( "AVLTreeMap unit testing..." )

    M = AVLTreeMap( )
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

#     M = AVLTreeMap( )
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

#     M = AVLTreeMap()
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

