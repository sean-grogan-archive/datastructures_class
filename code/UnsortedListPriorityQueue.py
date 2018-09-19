"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

from PriorityQueue import PriorityQueue

#UnsortedListPriorityQueue
class UnsortedListPriorityQueue( PriorityQueue ):

    #ADT and basic methods

    def __init__( self ):
        self._Q = []

    def __len__( self ):
        return len( self._Q )

    def __getitem__( self, i ):
        return self._Q[i]

    def is_empty( self ):
        return len( self ) == 0

    def min( self ):
        if self.is_empty():
            return False
        #search the min in O(n) on average
        the_min = self._Q[0]
        for item in self:
            if item < the_min:
                the_min = item
        #return the min
        return the_min

    def add( self, k, x ):
        #in O(1)
        self._Q.append( self._Item( k, x ) )

    def remove_min( self ):
        if self.is_empty():
            return False
        #search the index of min in O(n) on average
        index_min = 0
        for i in range( 1, len( self ) ):
            if self._Q[i] < self._Q[index_min]:
                index_min = i
        the_min = self._Q[index_min]
        #delete the min
        del self._Q[index_min]
        #return the deleted item
        return the_min
        
            
"""unit testing
"""
if __name__ == '__main__':

    print( "UnsortedListPriorityQueue unit testing..." )

    testQ = UnsortedListPriorityQueue()
    testQ.add( 5, 'A' )
    testQ.add( 9, 'C' )
    testQ.add( 3, 'B' )
    testQ.add( 7, 'D' )
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.remove_min()
    testQ.remove_min()
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.add( 2, 'AA' )
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.remove_min()
    testQ.remove_min()
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    print( testQ.remove_min() )

    print( "End of testing." )
