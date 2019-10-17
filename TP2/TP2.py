#!/usr/bin/env python
# encoding: utf-8
"""
TP2.py

Coéquipiers :
Sean Grogan
20001636

solo
"""
__author__ = 'Sean Grogan'

import unittest
from GenBinTrees import *
from BinaryTreeSeeder import *
from OptimalAreaFinder import *


def main(objets):
    # main return variable
    arbres = []

    # declaring all internal variables
    box_keys = []
    number_of_boxes = len(objets)
    tree_list = []

    # imports the objets key into a list
    for i in objets:
        box_keys.append(i[0])

    # generating the rotation box 2D array
    rotations_list = generate_rotations(number_of_boxes)

    # generating the permutations of the boxes (ie: ABC, BCA, BAC, ACB, etc...)
    box_key_permutations = permutation_boxes(box_keys)

    # generate the abstract binary trees
    # instead of having cutting planes | and/or - there will be @'s
    for i in box_key_permutations:
        for t in all_binary_trees(binary_tree_string(i)):
            tree = ''
            for s in t:
                if s in"'[]":
                    pass
                else:
                    tree += s
            tree_list.append(tree)

    temp2 = []
    # this will now convert the tree list into a more friendly list format!!
    for tree in tree_list:
        temp = string_to_list(tree)
        temp2.append(temp)

    tree_list = temp2

    # Seeding the trees with the cutting planes!
    # the following function can seed half or all the trees.
    # if it does half the trees it should cut the solve time in half.
    tree_list = binary_tree_seeder(tree_list)
    # now I should have all the trees in a list format so I can compute the area of the boxes

    # the following function will return the optimal area
    fin_tree = optimal_area_finder(tree_list, rotations_list, objets)
    # the above function will return only one tree and it is the mot optimal

    arbres.append(fin_tree)

    #RETURNS THE LIST!!!
    return arbres


#LEAVE ALONE! --------------------------------------------------------------------------------------------------
class TP2Tests(unittest.TestCase):
    def setUp(self):
        self.objets = []
        self.arbres = []

    def test1(self):
        self.objets = []
        self.objets.append(("AaA", 2, 7))
        self.objets.append(("BbB", 5, 3))
        self.arbres = []
        self.arbres.append('10:(-,AaA,BbB):35')
        self.arbres.append('10:(-,BbB,AaA):35')
        self.arbres.append('01:(|,AaA,BbB):35')
        self.arbres.append('01:(|,BbB,AaA):35')
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