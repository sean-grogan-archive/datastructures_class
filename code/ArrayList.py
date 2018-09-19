from DynamicArray import DynamicArray

class ArrayList:

    #implements the ADT List (List.py)
    #uses the DynamicArray class (DynamicArray.py)
    def __init__( self ):
        self._A = DynamicArray()

    def __len__( self ):
        return len( self._A )

    def __str__( self ):
        return str( self._A )

    def __getitem__( self, k ):
        return self._A[k]

    #append at the end of the list
    def append( self, obj ):
        self._A.append( obj )

    #remove the ith element of the list
    def remove( self, i ):
        return self._A.remove( i )

    #return the rank of obj in the list
    def find( self, obj ):
        return self._A.find( obj )

"""unit testing
"""
if __name__ == '__main__':

    data = ArrayList()
    print( data )

    data.append( 'titi' )
    data.append( 'toto' )
    data.append( 'tata' )
    print( data )

    idx = data.find( 'titi' )
    if idx:
        print( "found titi ranked", idx )
    else:
        print( "titi not found" )
    idx = data.find( 'cece' )
    if idx:
        print( "found cece ranked", idx )
    else:
        print( "cece not found" )

    print( "remove 1 =", data.remove( 1 ) )
    print( "new size = ", str( len( data ) ) )
    print( data )
    print( "remove 2 = ", data.remove( 2 ) )
    print( data )
    print( "remove 5 = ", data.remove( 5 ) )
    print( "remove 1 = ", data.remove( 1 ) )
    print( data )
    print( "remove 1 = ", data.remove( 1 ) )
    print( data )
