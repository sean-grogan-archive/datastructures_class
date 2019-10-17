from BinaryTree import BinaryTree


class LinkedBinaryTree( BinaryTree ):
    class _Node:
        #create a static structure for _Node using __slots__
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        def element(self):
            return self._element

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def __str__(self):
            return str(self._node._element)

        def element(self):
            return self._node._element

        def __eq__( self, other ):
            return type( other ) is type( self ) and other._node is self._node

    def _validate( self, p ):
        #return associated node if position is valid
        if not isinstance( p, self.Position ):
            raise TypeError( 'p must be proper Position type' )
        if p._container is not self:
            raise ValueError( 'p does not belong to this container' )
        if p._node._parent is p._node:
            raise ValueError( 'p is no longer valid' )
        return p._node

    def _make_position( self, node ):
        #return Position instance for given node (None if no node)
        return self.Position( self, node ) if node is not None else None

    def __init__( self ):
        #create an initially empty binary tree
        self._root = None
        self._size = 0

    def __len__( self ):
        return self._size

    def root( self ):
        return self._make_position( self._root )

    def parent( self, p ):
        node = self._validate( p )
        return self._make_position( node._parent )

    def left( self, p ):
        node = self._validate( p )
        return self._make_position( node._left )

    def right( self, p ):
        node = self._validate( p )
        return self._make_position( node._right )

    def num_children( self, p ):
        node = self._validate( p )
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root( self, e ):
        if self._root is not None: raise ValueError( 'Root exists' )
        self._size = 1
        self._root = self._Node( e )
        return self._make_position( self._root )

    def _add_left( self, p, e ):
        node = self._validate( p )
        if node._left is not None: raise ValueError( 'Left child exists' )
        self._size += 1
        node._left = self._Node( e, node )
        return self._make_position( node._left )

    def _add_right( self, p, e ):
        node = self._validate( p )
        if node._right is not None: raise ValueError( 'Right child exists' )
        self._size += 1
        node._right = self._Node( e, node )
        return self._make_position( node._right )

    def _replace( self, p, e ):
        node = self._validate( p )
        old = node._element
        node._element = e
        return old

    def _delete( self, p ):
        #remove the external node p
        node = self._validate( p )
        if self._num_children( p ) == 2: raise ValueError( 'p has two children' )
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach( self, p, t1, t2 ):
        node = self._validate( p )
        if not self.is_left( p ): raise ValueError( 'position must be leaf' )
        if not type( self ) is type( t1 ) is type( t2 ):
            raise TypeError( 'Tree types must match' )
        self._size += len( t1 ) + len( t2 )
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._left = t2._root
            t2._root = None
            t2._size = 0

    def tp2_print(self, p):
        if self.is_leaf(p):
            printer = str(p)
        else:
            lefty = self.tp2_print(self.left(p))
            righty = self.tp2_print(self.right(p))
            p = str(p)
            printer = '('+p+','+str(lefty)+','+str(righty)+')'
        return printer


"""unit testing
"""
if __name__ == '__main__':

    mytree = LinkedBinaryTree()

    tree_list = []

    mytree._add_root( "ROOT" )
    mytree.preorder_print( mytree.root() )

    mytree._add_left( mytree.root(), "01" )
    theright = mytree._add_right( mytree.root(), "02" )
    mytree._add_left( theright, "03" )
    theright = mytree._add_right( theright, "04" )
    mytree._add_left( theright, "05" )
    theright = mytree._add_right( theright, "06" )

    mytree.preorder_print( mytree.root() )
    mytree.postorder_print( mytree.root() )

    print( mytree.depth( mytree.root() ) )
    print( mytree.height( mytree.root() ) )

    mytree._replace( theright, "07" )
    print(mytree.parent(theright))
    mytree.preorder_print( mytree.root() )
    mytree.inorder_print( mytree.root() )
    mytree.breadth_first_print()
    theleft = mytree.left(mytree.root())

    mytree._add_left(theleft, "08")
    mytree._add_right(theleft, "09")

    print(mytree.parent(theright))
    print(mytree.tp2_print(mytree.root()))