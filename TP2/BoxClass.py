class BoxClass:
    """class for easy box handling"""
    def __init__(self, name, width, height):
        """init method"""
        self._name = name
        self._width = width
        self._height = height
        self._rotate = False

    def __lt__(self, other):
        """for sorting"""
        return self._name < other.name()

    def __gt__(self, other):
        """for sorting"""
        return self._name > other.name()

    def __eq__(self, other):
        """for sorting"""
        return self._name == other.name()

    def __str__(self):
        """pretty printing"""
        pp = '(' + self._name + ',' + str(self._width) + ',' + str(self._height) + ')'
        return pp

    def rotate_box(self):
        """class to rotate the box"""
        self._rotate = not self._rotate

    def reset_rotate(self):
        """rotates the box to original"""
        self._rotate = False

    def is_rotated(self):
        """class to tell if a box is rotated"""
        return self._rotate

    def name(self):
        """return thy name"""
        return self._name

    def height(self):
        """returns the height"""
        if self._rotate:
            return self._width
        else:
            return self._height

    def width(self):
        """returns the width"""
        if self._rotate:
            return self._height
        else:
            return self._width

# unit testing
if __name__ == '__main__':
    print('unit testing')
    box = BoxClass('A', 5, 3)
    print(box.height())
    print(box.is_rotated())
    box.rotate_box()
    print(box.height())
    print(box.is_rotated())
    print(box)