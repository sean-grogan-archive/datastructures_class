"""Programme pour le cours IFT2015
   Écrit par François Major le 9 février 2014.
"""

class ListList:

    #implements the ADT List (List.py)
    #uses the python default List
    def __init__( self ):
        self._A = []

    def __len__( self ):
        return len( self._A )

    #no access to a python's list capacity
    def __str__( self ):
        pp = str( self._A )
        pp += "(size = " + str( len( self._A ) ) + ")"
        return pp

    def __getitem__( self, k ):
        return self._A[k]

    #append at the end of the list
    def append( self, obj ):
        self._A.append( obj )

    #remove the ith element of the list
    def remove( self, i ):
        if len( self._A ) > 0:
            #indices in a python's list starts at 0
            self._A.pop( i-1 )
            return True
        else:
            return False

    #return the rank of obj in the list
    #or False otherwise
    def find( self, obj ):
        try:
            idx = self._A.index( obj )
        except ValueError:
            return False
        #obj is in the list
        #indices in a python's list starts at 0
        return 1 + self._A.index( obj )

"""unit testing
"""
if __name__ == '__main__':

    data = ListList()
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
    print( "remove 1 = ", data.remove( 1 ) )
    print( data )
    print( "remove 1 = ", data.remove( 1 ) )
    print( data )
