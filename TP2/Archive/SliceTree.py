import operator


class SliceTree:
    class Node:
        def __init__(self, name, key=None, left=None, right=None, parent=None):
            self._name = name
            self._key = key
            self._left = left
            self._right = right
            self._parent = parent

        def name(self):
            return self._name

        def key(self):
            return self._key

        def left(self):
            return self._left

        def right(self):
            return self._right

        def parent(self):
            return self._parent

        def is_root(self):
            return self._parent is None

        def is_leaf(self):
            return self._left is None and self._right is None

        def set_right(self, element):
            self._right = element

        def set_left(self, element):
            self._left = element

        def set_parent(self, element):
            self._parent = element

        def print_node(self):
            if self.is_leaf():
                printer = '('+self.name()+','+self.left()+','+self.right()+')'
            else:
                printer = self.name()
            return

    def __init__(self):
        self._tree = []
        self.key_counter = -1

    def add_node(self, name, key=None, left=None, right=None, parent=None):
        self.key_counter += 1
        if key is not None:
            self.key_counter += 1
            key = self.key_counter
            self._tree.insert(key, self.Node(name, key, left, right, parent))
        else:
            self._tree.insert(key, self.Node(name, key, left, right, parent))
        self.sort_tree()  # sorts the tree at the end of the document to ensure root is at top!

    def sort_tree(self):
        self._tree.sort(key=operator.attrgetter('key'))

    def print_tree(self):
        pass

