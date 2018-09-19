from DynamicArray import DynamicArray

class ArrayStack:

    #implements the ADT Stack (Stack.py)
    #uses the DynamicArray class (DynamicArray.py)
    def __init__( self ):
        self._A = DynamicArray()

    def __len__( self ):
        return len( self._A )

    def is_empty( self ):
        return len( self._A ) == 0

    def __str__( self ):
        pp = str( self._A )
        pp += "[top = " + str( len( self._A ) - 1 ) + ")"
        return pp

    #push obj
    def push( self, obj ):
        self._A.append( obj )

    #pop
    def pop( self ):
        return self._A.remove( len( self._A ) )

    #top
    def top( self ):
        return self._A.get( len( self._A ) )

"""unit testing
"""
if __name__ == '__main__':

    data = ArrayStack()
    print( data )

    data.push( 5 )
    print( "push 5" )
    print( data )

    data.push( 3 )
    print( "push 3" )
    print( data )

    print( "len = ", str( len( data ) ) )
    print( "pop = ", data.pop() )
    print( data )

    print( "empty? ", data.is_empty() )
    print( "pop = ", data.pop() )
    print( "empty? ", data.is_empty() )

    print( "pop = ", data.pop() )

    data.push( 7 )
    print( "push 7" )
    print( data )
    data.push( 9 )
    print( "push 9" )
    print( data )
    print( "top = ", data.top() )

    data.push( 4 )
    print( "push 4" )
    print( data )
    print( "len = ", len( data ) )
    print( "pop = ", data.pop() )
    print( data )
    data.push( 6 )
    print( "push 6" )
    data.push( 8 )
    print( "push 8" )
    print( data )
    print( "pop = ", data.pop() )

    print( data )
    print( "pop = ", data.pop() )
    print( "pop = ", data.pop() )
    print( "pop = ", data.pop() )
    print( "pop = ", data.pop() )
