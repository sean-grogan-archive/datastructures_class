"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

#ADT SkipList

import random
from SkipListNode import SkipListNode
from Coin import Coin

_FACE      = True
_TAILS     = False

class SkipList():

    def __init__( self, _MIN_VALUE = -999999999, _MAX_VALUE = 999999999 ):
        self._MIN_VALUE = _MIN_VALUE
        self._MAX_VALUE = _MAX_VALUE
        self._coin = Coin()
        self._height = 1
        self._count = 0
        sentinel_lr = SkipListNode( self._MAX_VALUE )
        sentinel_ll = SkipListNode( self._MIN_VALUE, None, sentinel_lr, None, None )
        sentinel_lr._prev = sentinel_ll
        sentinel_ul = SkipListNode( self._MIN_VALUE, None, None, sentinel_ll, None )
        sentinel_ur = SkipListNode( self._MAX_VALUE, sentinel_ul, None, sentinel_lr, None )
        sentinel_ul._next = sentinel_ur
        sentinel_ll._abov = sentinel_ul
        sentinel_lr._abov = sentinel_ur
        self._start = sentinel_ul

    #return the number of elements in List
    def __len__( self ):
        return self._count

    #convert a SkipList into a string:
    # elements listed between brackets
    # separated by commas.
    def __str__( self ):
        tower = self._start
        pp = "SkipList of height " + str( self._height ) + ":\n"
        for level in range( self._height, -1, -1 ):
            p = tower
            pp += "level " + str( level ) + " [" + str( p._elem )
            p = p._next
            while not( p is None ):
                pp +=  "," + str( p._elem )
                p = p._next
            tower = tower._belo
            pp += "]\n"
        return pp

    def __iter__( self ):
        tower = self._start
        while not( tower._belo is None ):
            tower = tower._belo
        tower = tower._next
        while not( tower._next is None ):
                yield tower._elem
                tower = tower._next

    def Min( self ):
        if self._count == 0:
            return False
        tower = self._start
        while not( tower._belo is None ):
            tower = tower._belo
        return tower._next._elem

    def Max( self ):
        if self._count == 0:
            return False
        tower = self._start
        while not( tower._belo is None ):
            tower = tower._belo
        tower = tower._next
        while not( tower._next is None ):
                tower = tower._next
        return tower._prev._elem()

    #search element
    def SkipSearch( self, element ):
        p = self._start
        while not( p._belo is None ):
            p = p._belo
            while element >= p._next._elem:
                p = p._next
        return p

    def increaseHeight( self ):
        old_sentinel_l = self._start
        old_sentinel_r = self._start._next
        new_sentinel_l = SkipListNode( self._MIN_VALUE, None, None, old_sentinel_l, None )
        new_sentinel_r = SkipListNode( self._MAX_VALUE, new_sentinel_l, None, old_sentinel_r, None )
        new_sentinel_l._next = new_sentinel_r
        old_sentinel_l._abov = new_sentinel_l
        old_sentinel_r._abov = new_sentinel_r
        self._height += 1
        self._start = new_sentinel_l

    def insertAfterAbove( self, p, q, element ):
        newnode = SkipListNode( element, p, p._next, q, None )
        p._next._prev = newnode
        p._next = newnode
        if not( q is None ):
            q._abov = newnode
        return newnode

    #insert element
    def SkipInsert( self, element ):
        p = self.SkipSearch( element )
        if p._elem == element:
            p._elem = element
            return p
        q = self.insertAfterAbove( p, None, element )
        i = 0
        coin_flip = self._coin.flip()
        while coin_flip == _FACE:
            i += 1
            if i >= self._height:
                self.increaseHeight()
            while p._abov is None:
                p = p._prev
            p = p._abov
            q = self.insertAfterAbove( p, q, element )
            coin_flip = self._coin.flip()
        self._count += 1
        return q

    #remove element
    def SkipRemove( self, element ):
        p = self.SkipSearch( element )
        if p._elem == element:
            tower = p
            while not( tower is None ):
                tower._prev._next = tower._next
                tower._next._prev = tower._prev
                tower = tower._abov
            return p
        return False

"""unit testing
"""
if __name__ == '__main__':

    print( "SkipList unit testing..." )

    L = SkipList()
    for i in range( 100 ):
        x = random.randint( 0, 100 )
        L.SkipInsert( x )
        print( L )
        print( str( L.SkipSearch( x ) ) )    
        
    print( "end unit testing..." )
