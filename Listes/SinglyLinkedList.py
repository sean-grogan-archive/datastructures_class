from SinglyLinkedNode import SinglyLinkedNode

class SinglyLinkedList:

    #implements the ADT List (List.py)
    #uses the SinglyLinkedNode class (SinglyLinkedNode.py)

    def __init__( self ):
        self._head = None
        self._last = None
        self._size = 0

    def __len__( self ):
        return self._size

    def __str__( self ):
        if self.is_empty():
            return "[](size = 0)"
        else:
            pp = "["
            curr = self._head
            while curr != self._last:
                pp += str( curr.element ) + ", "
                curr = curr.next
            pp += str( curr.element ) + "]"
            pp += "(size = " + str( self._size ) + ")"
        return pp

    def is_empty( self ):
        return self._size == 0

    def append( self, element ):
        newNode = SinglyLinkedNode( element, None )
        if self._last == None:
            self._head = self._last = newNode
        else:
            self._last.next = newNode
            self._last = newNode
        self._size += 1

    def insert( self, element ):
        newNode = SinglyLinkedNode( element, self._head )
        if self._head == None:
            self._last = newNode
        self._head = newNode
        self._size += 1

    def remove( self, k ):
        if self.is_empty():
            return False
        else:
            curr = self._head
            prev = None
            for i in range( k - 1 ):
                prev = curr
                curr = curr.next
            if prev == None:
                #remove the first element
                self._head = curr.next
            else:
                prev.next = None
                self._last = prev
            self._size -= 1
            if self._size == 0:
                self._last = None
            return curr.element

    def find( self, element ):
        if self.is_empty():
            return False
        else:
            curr = self._head
            for i in range( self._size ):
                if curr.element == element:
                    return i + 1
                else:
                    curr = curr.next

    def last( self ):
        if self.is_empty():
            return False
        else:
            return self._last.element

    def first( self ):
        if self.is_empty():
            return False
        else:
            return self._head.element

"""unit testing
"""
if __name__ == '__main__':

    data = SinglyLinkedList()
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
    

                
        
