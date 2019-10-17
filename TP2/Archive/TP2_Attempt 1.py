#!/usr/bin/env python
# encoding: utf-8
"""
TP2.py

Coéquipiers :
Sean Grogan
20001636

Alone
"""

import unittest
import LinkedBinaryTree
import math
import random

def main(objets):
    
    arbres = []
    binary_trees = []

    boxes = []
    num_boxes = len(objets)
    for i in range(num_boxes):
        boxes.append(NodeClass(objets[i][0], objets[i][1], objets[i][2]))

    rotations = generate_rotations(num_boxes)  # makes a list of zeros and ones to test in the tree

    for i in range(math.factorial(num_boxes)):
        pass

    tree_1 = []
    tree_1.append(NodeClass('|'))
    for i in range(num_boxes-1):
        if i%2 == 1:
            tree_1[i].set_right(NodeClass('|', i-1))
            tree_1.append(NodeClass('|'))
        else:
            tree_1[i].set_right(NodeClass('-', i-1))
        tree_1[i].set_left(NodeClass(boxes[i].name(), i-1))

    print(tree_1[0].tree_out())
    return arbres


def generate_rotations(num):
    """generates all the rotations of a given problem set"""
    _rotations = []
    for i in range(2**num):
        b = []
        temp = '{:0'+str(num)+'b}'
        for k in str(temp.format(i)):
            b.append(int(k))
        _rotations.append(b)
    return _rotations


def width_element(element):
    """part of the algorithm for determining w(p)"""
    if element.is_leaf():
        return element.w()
    elif element.name() is '-':
        return max(element.left().w(), element.right().w())
    elif element.name() is '|':
        return element.left().w() + element.right().w()
    else:
        print('error 101')


def height_element(element):
    """part of the algorithm for determining h(p)"""
    if element.is_leaf():
        return element.h()
    elif element.name() is '-':
        return element.left().h() + element.right().h()
    elif element.name() is '|':
        return max(element.left().h(), element.right().h())
    else:
        print('error 102')


class SlicingFloorPlan:
    """class for the slicing floor plan as defined on page 360 in the book"""
    def __init__(self):
        """init class"""
        self.basic_rect = []
        self.tree = []
        self.min_height = None
        self.min_width = None

    def horizontal_cut(self, left, right):
        """creates a horizontal cut"""
        self.tree.append(('-', left, right))

    def vertical_cut(self, left, right):
        """creates a vertical cut"""
        self.tree.append(('|', left, right))

    def assign_min_height(self, height):
        """assigns min height"""
        self.min_height = height

    def assign_min_width(self, width):
        """assigns min width"""
        self.min_height = width

    def draw_tree(self):
        """draws the tree"""
        return self.tree


class LeafClass:
    """class for leaves"""
    def __init__(self, name, width, height):
        """init class for the leaf"""
        self._name = name
        self._x = None
        self._y = None
        self._h = height
        self._w = width
        self._direction = True  # initial direction setting to true, will change to false if turned

    def __str__(self):
        return self._name


class NodeClass:
    def __init__(self, name, parent = None, width = None, height = None):
        """init class for the node"""
        self._name = name
        self._left = None
        self._right = None
        self._parent = parent
        self._x = None
        self._y = None
        self._h = height
        self._w = width
        self._direction = True  # initial direction setting to true, will change to false if turned

    def __str__(self):
        returned = '(' + str(self._name) + ',' + str(self._right) + ',' + str(self._left) + ')'
        return returned

    def name(self):
        """return ID"""
        return self._name

    def right(self):
        """returning the right element"""
        if self._right is not None:
            return self._right
        else:
            return False

    def left(self):
        """returning the left element"""
        if self._left is not None:
            return self._left
        else:
            return False

    def parent(self):
        """returns the parent of the node, should probably be the index of the array you use"""
        return self._parent

    def is_leaf(self):
        """true false for the element"""
        if self._right is None and self._left is None:
            return True
        else:
            return False

    def set_x(self, x_coordinate):
        self._x = x_coordinate

    def set_y(self, y_coordinate):
        self._y = y_coordinate

    def tree_out(self):
        if self.is_leaf():
            returned = str(self._name)
        else:
            returned = '(' + str(self._name) + ',' + str(self._right) + ',' + str(self._left) + ')'
        return returned

    def orientation(self):
        """returns the orientation of the box"""
        if self._direction:
            return 0  # returns zero 0 if the box is in its original orientation
        else:
            return 1  # returns one 1 if the box is rotated

    def rotate(self):
        """rotate the box"""
        self._direction = not self._direction

    def h(self):
        """return h size"""
        if self.orientation() is 0:
            return self._h
        else:
            return self._w

    def w(self):
        """return w size"""
        if self.orientation() is 0:
            return self._w
        else:
            return self._h

    def set_left(self, name):
        self._left = name

    def set_right(self, name):
        self._right = name

    def set_parent(self, name):
        self._parent = name


#LEAVE ALONE! --------------------------------------------------------------------------------------------------
class TP2Tests(unittest.TestCase):
    def setUp(self):
        self.objets = []
        self.arbres = []
            
    def test1(self):
        self.objets = []
        self.objets.append(("A", 2, 7))
        self.objets.append(("B", 5, 3))
        self.arbres = []
        self.arbres.append('10:(-,A,B):35')
        self.arbres.append('10:(-,B,A):35')
        self.arbres.append('01:(|,A,B):35')
        self.arbres.append('01:(|,B,A):35')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test2(self):
        self.objets = []
        self.objets.append(("A", 2, 13))
        self.objets.append(("B", 11, 3))
        self.objets.append(("C", 5, 7))
        self.arbres = []
        self.arbres.append('101:(|,(-,A,B),C):100')
        self.arbres.append('101:(|,(-,B,A),C):100')
        self.arbres.append('101:(|,C,(-,A,B)):100')
        self.arbres.append('101:(|,C,(-,B,A)):100')
        self.arbres.append('010:(-,(|,A,B),C):100')
        self.arbres.append('010:(-,(|,B,A),C):100')
        self.arbres.append('010:(-,C,(|,A,B)):100')
        self.arbres.append('010:(-,C,(|,B,A)):100')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test3(self):
        self.objets = []
        self.objets.append(("A", 1, 1))
        self.objets.append(("B", 2, 1))
        self.objets.append(("C", 1, 3))
        self.arbres = []
        self.arbres.append('110:(|,(-,A,B),C):6')
        self.arbres.append('110:(|,(-,B,A),C):6')
        self.arbres.append('110:(|,C,(-,A,B)):6')
        self.arbres.append('110:(|,C,(-,B,A)):6')
        self.arbres.append('101:(-,(|,A,B),C):6')
        self.arbres.append('101:(-,(|,B,A),C):6')
        self.arbres.append('101:(-,C,(|,A,B)):6')
        self.arbres.append('101:(-,C,(|,B,A)):6')
        self.arbres.append('010:(|,(-,A,B),C):6')
        self.arbres.append('010:(|,(-,B,A),C):6')
        self.arbres.append('010:(|,C,(-,A,B)):6')
        self.arbres.append('010:(|,C,(-,B,A)):6')
        self.arbres.append('001:(-,(|,A,B),C):6')
        self.arbres.append('001:(-,(|,B,A),C):6')
        self.arbres.append('001:(-,C,(|,A,B)):6')
        self.arbres.append('001:(-,C,(|,B,A)):6')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test4(self):
        self.objets = []
        self.objets.append(("A", 1, 1))
        self.objets.append(("B", 2, 1))
        self.objets.append(("C", 2, 3))
        self.arbres = []
        self.arbres.append('110:(|,(-,A,B),C):9')
        self.arbres.append('110:(|,(-,B,A),C):9')
        self.arbres.append('110:(|,C,(-,A,B)):9')
        self.arbres.append('110:(|,C,(-,B,A)):9')
        self.arbres.append('101:(-,(|,A,B),C):9')
        self.arbres.append('101:(-,(|,B,A),C):9')
        self.arbres.append('101:(-,C,(|,A,B)):9')
        self.arbres.append('101:(-,C,(|,B,A)):9')
        self.arbres.append('010:(|,(-,A,B),C):9')
        self.arbres.append('010:(|,(-,B,A),C):9')
        self.arbres.append('010:(|,C,(-,A,B)):9')
        self.arbres.append('010:(|,C,(-,B,A)):9')
        self.arbres.append('001:(-,(|,A,B),C):9')
        self.arbres.append('001:(-,(|,B,A),C):9')
        self.arbres.append('001:(-,C,(|,A,B)):9')
        self.arbres.append('001:(-,C,(|,B,A)):9')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)

    def test5(self):
        self.objets = []
        self.objets.append(("A", 1, 2))
        self.objets.append(("B", 3, 2))
        self.objets.append(("C", 3, 4))
        self.arbres = []
        self.arbres.append('110:(|,(-,A,B),C):20')
        self.arbres.append('110:(|,(-,B,A),C):20')
        self.arbres.append('110:(|,C,(-,A,B)):20')
        self.arbres.append('110:(|,C,(-,B,A)):20')
        self.arbres.append('001:(-,(|,A,B),C):20')
        self.arbres.append('001:(-,(|,B,A),C):20')
        self.arbres.append('001:(-,C,(|,A,B)):20')
        self.arbres.append('001:(-,C,(|,B,A)):20')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test6(self):
        self.objets = []
        self.objets.append(("A", 2, 19))
        self.objets.append(("B", 17, 3))
        self.objets.append(("C", 5, 13))
        self.objets.append(("D", 11, 7))
        self.arbres = []
        self.arbres.append('1010:(-,A,(|,(-,B,C),D)):280')
        self.arbres.append('1010:(-,A,(|,(-,C,B),D)):280')
        self.arbres.append('1010:(-,A,(|,D,(-,B,C))):280')
        self.arbres.append('1010:(-,A,(|,D,(-,C,B))):280')
        self.arbres.append('1010:(-,(|,(-,B,C),D),A):280')
        self.arbres.append('1010:(-,(|,(-,C,B),D),A):280')
        self.arbres.append('1010:(-,(|,D,(-,B,C)),A):280')
        self.arbres.append('1010:(-,(|,D,(-,C,B)),A):280')
        self.arbres.append('0101:(|,A,(-,(|,B,C),D)):280')
        self.arbres.append('0101:(|,A,(-,(|,C,B),D)):280')
        self.arbres.append('0101:(|,A,(-,D,(|,B,C))):280')
        self.arbres.append('0101:(|,A,(-,D,(|,C,B))):280')
        self.arbres.append('0101:(|,(-,(|,B,C),D),A):280')
        self.arbres.append('0101:(|,(-,(|,C,B),D),A):280')
        self.arbres.append('0101:(|,(-,D,(|,B,C)),A):280')
        self.arbres.append('0101:(|,(-,D,(|,C,B)),A):280')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test7(self):
        self.objets = []
        self.objets.append(("A", 1, 2))
        self.objets.append(("B", 2, 3))
        self.objets.append(("C", 3, 4))
        self.objets.append(("D", 4, 5))
        self.arbres = []
        self.arbres.append('1001:(-,(|,(-,A,B),C),D):40')
        self.arbres.append('1001:(-,(|,(-,B,A),C),D):40')
        self.arbres.append('1001:(-,(|,C,(-,A,B)),D):40')
        self.arbres.append('1001:(-,(|,C,(-,B,A)),D):40')
        self.arbres.append('1001:(-,D,(|,(-,A,B),C)):40')
        self.arbres.append('1001:(-,D,(|,(-,B,A),C)):40')
        self.arbres.append('1001:(-,D,(|,C,(-,A,B))):40')
        self.arbres.append('1001:(-,D,(|,C,(-,B,A))):40')
        self.arbres.append('0110:(|,(-,(|,A,B),C),D):40')
        self.arbres.append('0110:(|,(-,(|,B,A),C),D):40')
        self.arbres.append('0110:(|,(-,C,(|,A,B)),D):40')
        self.arbres.append('0110:(|,(-,C,(|,B,A)),D):40')
        self.arbres.append('0110:(|,D,(-,(|,A,B),C)):40')
        self.arbres.append('0110:(|,D,(-,(|,B,A),C)):40')
        self.arbres.append('0110:(|,D,(-,C,(|,A,B))):40')
        self.arbres.append('0110:(|,D,(-,C,(|,B,A))):40')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test8(self):
        self.objets = []
        self.objets.append(("A", 2, 29))
        self.objets.append(("B", 23, 3))
        self.objets.append(("C", 5, 19))
        self.objets.append(("D", 17, 7))
        self.objets.append(("E", 11, 13))
        self.arbres = []
        self.arbres.append('10101:(|,(-,A,(|,(-,B,C),D)),E):583')
        self.arbres.append('10101:(|,(-,A,(|,(-,C,B),D)),E):583')
        self.arbres.append('10101:(|,(-,A,(|,D,(-,B,C))),E):583')
        self.arbres.append('10101:(|,(-,A,(|,D,(-,C,B))),E):583')
        self.arbres.append('10101:(|,(-,(|,(-,B,C),D),A),E):583')
        self.arbres.append('10101:(|,(-,(|,(-,C,B),D),A),E):583')
        self.arbres.append('10101:(|,(-,(|,D,(-,B,C)),A),E):583')
        self.arbres.append('10101:(|,(-,(|,D,(-,C,B)),A),E):583')
        self.arbres.append('10101:(|,E,(-,A,(|,(-,B,C),D))):583')
        self.arbres.append('10101:(|,E,(-,A,(|,(-,C,B),D))):583')
        self.arbres.append('10101:(|,E,(-,A,(|,D,(-,B,C)))):583')
        self.arbres.append('10101:(|,E,(-,A,(|,D,(-,C,B)))):583')
        self.arbres.append('10101:(|,E,(-,(|,(-,B,C),D),A)):583')
        self.arbres.append('10101:(|,E,(-,(|,(-,C,B),D),A)):583')
        self.arbres.append('10101:(|,E,(-,(|,D,(-,B,C)),A)):583')
        self.arbres.append('10101:(|,E,(-,(|,D,(-,C,B)),A)):583')
        self.arbres.append('01010:(-,(|,A,(-,(|,B,C),D)),E):583')
        self.arbres.append('01010:(-,(|,A,(-,(|,C,B),D)),E):583')
        self.arbres.append('01010:(-,(|,A,(-,D,(|,B,C))),E):583')
        self.arbres.append('01010:(-,(|,A,(-,D,(|,C,B))),E):583')
        self.arbres.append('01010:(-,(|,(-,(|,B,C),D),A),E):583')
        self.arbres.append('01010:(-,(|,(-,(|,C,B),D),A),E):583')
        self.arbres.append('01010:(-,(|,(-,D,(|,B,C)),A),E):583')
        self.arbres.append('01010:(-,(|,(-,D,(|,C,B)),A),E):583')
        self.arbres.append('01010:(-,E,(|,A,(-,(|,B,C),D))):583')
        self.arbres.append('01010:(-,E,(|,A,(-,(|,C,B),D))):583')
        self.arbres.append('01010:(-,E,(|,A,(-,D,(|,B,C)))):583')
        self.arbres.append('01010:(-,E,(|,A,(-,D,(|,C,B)))):583')
        self.arbres.append('01010:(-,E,(|,(-,(|,B,C),D),A)):583')
        self.arbres.append('01010:(-,E,(|,(-,(|,C,B),D),A)):583')
        self.arbres.append('01010:(-,E,(|,(-,D,(|,B,C)),A)):583')
        self.arbres.append('01010:(-,E,(|,(-,D,(|,C,B)),A)):583')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test9(self):
        self.objets = []
        self.objets.append(("A", 2, 37))
        self.objets.append(("B", 31, 3))
        self.objets.append(("C", 5, 29))
        self.objets.append(("D", 23, 7))
        self.objets.append(("E", 11, 19))
        self.objets.append(("F", 17, 13))
        self.arbres = []
        self.arbres.append('101010:(-,(|,(-,A,(|,D,E)),F),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,(-,A,(|,D,E)),F),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,(-,A,(|,E,D)),F),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,(-,A,(|,E,D)),F),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,(-,A,(|,D,E)),F)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,(-,A,(|,E,D)),F)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,(-,(|,D,E),A),F)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,(-,(|,E,D),A),F)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,F,(-,A,(|,D,E)))):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,F,(-,A,(|,E,D)))):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,F,(-,(|,D,E),A))):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,F,(-,(|,E,D),A))):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,(-,A,(|,D,E)),F)):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,(-,A,(|,E,D)),F)):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,(-,(|,D,E),A),F)):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,(-,(|,E,D),A),F)):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,F,(-,A,(|,D,E)))):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,F,(-,A,(|,E,D)))):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,F,(-,(|,D,E),A))):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,F,(-,(|,E,D),A))):1080')
        self.arbres.append('101010:(-,(|,(-,(|,D,E),A),F),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,(-,(|,D,E),A),F),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,(-,(|,E,D),A),F),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,(-,(|,E,D),A),F),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,F,(-,A,(|,D,E))),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,F,(-,A,(|,D,E))),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,F,(-,A,(|,E,D))),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,F,(-,A,(|,E,D))),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,F,(-,(|,D,E),A)),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,F,(-,(|,D,E),A)),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,F,(-,(|,E,D),A)),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,F,(-,(|,E,D),A)),(|,C,B)):1080')
        self.arbres.append('010101:(|,(-,(|,A,(-,D,E)),F),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,(|,A,(-,D,E)),F),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,(|,A,(-,E,D)),F),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,(|,A,(-,E,D)),F),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,(|,A,(-,D,E)),F)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,(|,A,(-,E,D)),F)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,(|,(-,D,E),A),F)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,(|,(-,E,D),A),F)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,F,(|,A,(-,D,E)))):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,F,(|,A,(-,E,D)))):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,F,(|,(-,D,E),A))):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,F,(|,(-,E,D),A))):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,(|,A,(-,D,E)),F)):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,(|,A,(-,E,D)),F)):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,(|,(-,D,E),A),F)):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,(|,(-,E,D),A),F)):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,F,(|,A,(-,D,E)))):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,F,(|,A,(-,E,D)))):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,F,(|,(-,D,E),A))):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,F,(|,(-,E,D),A))):1080')
        self.arbres.append('010101:(|,(-,(|,(-,D,E),A),F),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,(|,(-,D,E),A),F),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,(|,(-,E,D),A),F),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,(|,(-,E,D),A),F),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,F,(|,A,(-,D,E))),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,F,(|,A,(-,D,E))),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,F,(|,A,(-,E,D))),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,F,(|,A,(-,E,D))),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,F,(|,(-,D,E),A)),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,F,(|,(-,D,E),A)),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,F,(|,(-,E,D),A)),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,F,(|,(-,E,D),A)),(-,C,B)):1080')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
if __name__ == '__main__':

    unittest.main()