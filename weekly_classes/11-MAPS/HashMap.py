"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

from Map import Map
from random import randrange

class HashMap( Map ):

    def __init__( self, cap = 11, p = 109345121 ):
        self._T = cap * [None]
        self._n = 0                          #number of entries in the map
        self._prime = p                      #prime for MAD compression
        self._scale = 1 + randrange( p - 1 ) #scale from 1 to p-1 for MAD
        self._shift = randrange( p )         #shift from 0 to p-1 for MAD

    def _hash_function( self, k ):
        return( hash( k ) * self._scale + self._shift ) % self._prime % len( self._T )

    def __len__( self ):
        return self._n

    def __getitem__( self, k ):
        j = self._hash_function( k )
        return self._bucket_getitem( j, k )

    def __setitem__( self, k, v ):
        j = self._hash_function( k )
        self._bucket_setitem( j, k, v )
        if self._n > len( self._T ) // 2:
            self._resize( 2 * len( self._T ) - 1 )

    def __delitem__( self, k ):
        j = self._hash_function( k )
        self._bucket_delitem( j, k )
        self._n -= 1

    def _resize( self, c ):
        old = list( self.items() )
        self._T = c * [None]
        self._n = 0
        for (k,v) in old:
            self[k] = v
