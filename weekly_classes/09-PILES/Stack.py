#ADT Stack "interface"
class Stack:

    def __init__( self ):
        pass

    #return the number of elements in Stack
    def __len__( self ):
        pass

    #convert a Stack into a string:
    # elements listed between brackets
    # separated by commas
    # top element highlighted
    # size and capacity of the data structure
    # indicated when relevant
    def __str__( self ):
        pass

    #indicate whether no element are
    #stored in the Stack
    def is_empty( self ):
        pass

    #add element on the Stack
    def push( self, element ):
        pass

    #remove an element from the Stack
    def pop( self ):
        pass

    #return the last inserted element
    #without removing it
    def top( self ):
        pass
