"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

class SkipListNode:

    __slots__ = '_elem', '_prev', '_next', '_belo', '_abov'
    def __init__( self, elem, prev = None, next = None, belo = None, abov = None ):
        self._elem = elem
        self._prev = prev
        self._next = next
        self._belo = belo
        self._abov = abov

    def __str__( self ):
        return "(" + str( self._elem ) + ")"
