from DoublyLinkedNode import DoublyLinkedNode

class DoublyLinkedList:

    #implements the ADT List (List.py)
    #uses the DoublyLinkedNode class (DoublyLinkedNode.py)

    def __init__( self ):
        self._head = DoublyLinkedNode( None, None, None )
        self._trail = DoublyLinkedNode( None, None, None )
        self._head.next = self._trail
        self._trail.prev = self._head
        self._size = 0

    def __len__( self ):
        return self._size

    def __str__( self ):
        if self.is_empty():
            return "[](size = 0)"
        else:
            pp = "["
            curr = self._head.next
            while curr.next != self._trail:
                pp += str( curr.element ) + ", "
                curr = curr.next
            pp += str( curr.element ) + "]"
            pp += "(size = " + str( self._size ) + ")"
        return pp

    def is_empty( self ):
        return self._size == 0

    def append( self, element ):
        newNode = DoublyLinkedNode( element, self._trail.prev, self._trail )
        self._trail.prev.next = newNode
        self._trail.prev = newNode
        self._size += 1

    def insert( self, element ):
        newNode = DoublyLinkedNode( element, self._head, self._head.next )
        self._head.next.prev = newNode
        self._head.next = newNode
        self._size += 1

    def remove( self, k ):
         if self.is_empty():
             return False
         elif k <= 0 or k > self._size:
             return False
         else:
             curr = self._head.next
             for i in range( k - 1 ):
                 curr = curr.next
             curr.prev.next = curr.next
             curr.next.prev = curr.prev
             self._size -= 1
             return curr.element

    def find( self, element ):
         if self.is_empty():
             return False
         else:
             curr = self._head.next
             for i in range( self._size ):
                 if curr.element == element:
                     return i + 1
                 else:
                    curr = curr.next

    def last( self ):
        if self.is_empty():
            return False
        else:
            return self._trail.prev.element

    def first( self ):
        if self.is_empty():
            return False
        else:
            return self._head.next.element

"""unit testing
"""
if __name__ == '__main__':

    data = DoublyLinkedList()
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

    data.append( 'titi' )
    data.append( 'toto' )
    data.append( 'tata' )
    data.append( 'hala' )
    data.append( 'asma' )
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

    print( "remove 3 =", data.remove( 3 ) )
    print( "new size = ", str( len( data ) ) )
    print( data )
    

                
        
