"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

from Map import Map
from SkipList import SkipList
import random
import time

class SkipListMap( Map ):

    def __init__( self, _MIN_VALUE, _MAX_VALUE ):
        self._T = SkipList( Map._Item( _MIN_VALUE, None ), Map._Item( _MAX_VALUE, None ) )

    def __str__( self ):
        return str( self._T )

    def __len__( self ):
        return len( self._T )

    def __getitem__( self, k ):
        p = self._T.SkipSearch( self._Item( k ) )
        if p._elem._key != k:
            return False
        return p._elem._value

    def __setitem__( self, k, v ):
        self._T.SkipInsert( self._Item( k, v ) )

    def __delitem__( self, k ):
        p = self._T.SkipRemove( self._Item( k ) )
        if p is None:
            return False
        return p._elem._value

    def __iter__( self ):
        for item in self._T:
            yield item._key

    def __reversed__( self ):
        for item in reversed( self._T ):
            yield item._key

    def pop( self, k ):
        p = self._T.SkipRemove( self._Item( k ) )
        if p is None:
            return False
        return p._elem._value

    def find_min( self ):
        if len( self._T ) > 0:
            theItem = self._T.Min()
            return (theItem._key, theItem._value)
        else:
            return None

    def find_max( self ):
        if len( self._T ) > 0:
            theItem = self._T.Max()
            return (theItem._key, theItem._value)
        else:
            return None

    def find_ge( self, k ):
        #return (key,value) where key >= k
        p = self._T.SkipSearch( Map._Item( k ) )
        if p._next is None:
            return None
        if p._elem._key < k:
            p = p._next
        return (p._elem._key,p._elem._value)

    def find_le( self, k ):
        #return (key,value) where key <= k
        p = self._T.SkipSearch( Map._Item( k ) )
        if p._prev is None:
            return None
        return (p._elem._key,p._elem._value)

    def find_gt( self, k ):
        #return (key,value) where key > k
        p = self._T.SkipSearch( Map._Item( k ) )
        if p._next is None or p._next._next is None:
            return None
        p = p._next
        return (p._elem._key,p._elem._value)

    def find_lt( self, k ):
        #return (key,value) where key < k
        p = self._T.SkipSearch( Map._Item( k ) )
        if p._prev is None or p._prev._prev is None:
            return None
        if p._elem._key == k:
            p = p._prev
        return (p._elem._key,p._elem._value)

    def find_range( self, start, stop ):
        #iterate (key,value) where start <= key < stop
        if start is None:
            start = self._T.Min()
        p = self._T.SkipSearch( Map._Item( start ) )
        if p._next is None:
            return None
        if p._elem._key < start:
            p = p._next
        while not( p._next is None ) and ( p._elem._key < stop ):
                yield (p._elem._key,p._elem._value)
                p = p._next

"""unit testing
"""
if __name__ == '__main__':

    print( "SkipListMap unit testing..." )

    M = SkipListMap( -999999999, 999999999 )
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



#     M = SkipListMap( "A", "Z" )
#     print( len( M ) ) #0
#     M['K'] = 2
#     M['B'] = 4
#     M['U'] = 2
#     M['V'] = 8
#     M['K'] = 9
#     print( M )
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

#     M = SkipListMap( -999999999, 999999999 )
#     nb = 50
#     random.seed( 131341 )
#     avant = time.time()
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         M[key] = key
#     apres = time.time()
#     print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )
#     print( "Skip List Height for ", nb, "keys is ", M._T._height, "." )
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
