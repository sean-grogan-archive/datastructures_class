#ADT List "interface"
class List:

    def __init__( self ):
        pass

    #return the number of elements in List
    def __len__( self ):
        pass

    #convert a List into a string:
    # elements listed between brackets
    # separated by commas
    # size and capacity of the data structure
    # indicated when relevant
    def __str__( self ):
        pass

    #add element at the end of list
    def append( self, element ):
        pass

    #remove the kth element
    def remove( self, k ):
        pass

    #find and return the rank of
    #element if in list, False otherwise
    def find( self, element ):
        pass
