"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

from PriorityQueue import PriorityQueue

#SortedListPriorityQueue
class SortedListPriorityQueue( PriorityQueue ):

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
        #find min in O(1)
        #the min is in Q[0]
        return self._Q[0]

    def add( self, k, x ):
        item = self._Item( k, x )
        if self.is_empty():
            self._Q.append( item )
        else:
            #create the extra space in Q
            self._Q.append( item )
            #search for insertion index
            #in O(n) on average
            i = 0
            while item > self._Q[i]:
                i += 1
            #make space for new item
            #in O(n) on average
            for j in range( len( self ) - 1, i, -1 ):
                self._Q[j] = self._Q[j-1]
            #insert item at insertion index
            self._Q[i] = item
        #return new item
        return item

    def remove_min( self ):
        if self.is_empty():
            return False
        #remove min in O(1)
        #the min is in Q[0]
        the_min = self._Q[0]
        del self._Q[0]
        return the_min
        
            
"""unit testing
"""
if __name__ == '__main__':

    print( "SortedListPriorityQueue unit testing..." )

    testQ = SortedListPriorityQueue()
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
