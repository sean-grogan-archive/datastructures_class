class SlicingTree:
    """tree class for the slicing tree"""
#_________________________________ Nested Node Class _________________________________#
    class _Node:
        """lightweight class for storing a node"""
        __slots__ = '_name', '_parent', '_left', '_right'  # streamline memory usage

        def __init__(self, name, parent=None, left=None, right=None):
            self._name = name  # initializes the node's fields
            self._parent = parent
            self._left = left
            self._right = right

#___________________________________ Tree Methods ____________________________________#
    def __init__(self):
        """create an initially empty binary tree"""
        self._root = None  # references to the head node
        self._size = 0     # initializes the size to ZERO

    def __len__(self):
        """Override of the __len__ class, returns number of elements"""
        return self._size

    def is_empty(self):
        """returns the result of the question, is_empty?"""
        return self._size == 0

    def is_leaf(self):
        """answers if the node a leaf"""
        if self._Node._left is None and self._Node._right is None:
            return True
        else:
            return False

    def add_root(self, name):
        """adds a root to the tree"""
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(name)
        self._size = 1

    def add_left(self, name, parent):
        """adds a left node to the tree"""
        if _Node._left is not None:
            raise ValueError( 'Left child exists' )
        left_node = self._Node(name, parent)
        self._Node._left = left_node
        self._size += 1

    def add_right(self, name, parent):
        """adds a right node to the tree"""
        right_node = self._Node(name, parent)
        self._Node._right = right_node
        self._size += 1
