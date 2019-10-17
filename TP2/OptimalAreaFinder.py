#!/usr/bin/env python
__author__ = 'Sean Grogan'
from BoxClass import *


def optimal_area_finder(tree_list, rotation_list, objets):
    """shell function for the optimal area finder"""
    box_list = []
    best_tree = ''
    best_area = float('inf')
    for box in objets:
        box_list.append(BoxClass(box[0], box[1], box[2]))
    for tree in tree_list:
        for rotation in rotation_list:
            new_area = area_finder(tree, rotation, box_list)
            if new_area <= best_area:
                best_tree = tree_to_string(tree, rotation, new_area)
                best_area = new_area

    print('best tree:', best_tree)
    return best_tree


def tree_to_string(tree, rotation, area):
    """converts the tree into a string format for returning"""
    tree_string = ''
    for i in rotation:
        tree_string += str(i)
    tree_string += ':'
    temp = str(tree)
    for i in temp:
        if i in '[{':
            tree_string += '('
        elif i in ']}':
            tree_string += ')'
        elif i in "'":
            pass
        elif i in " ":
            pass
        else:
            tree_string += i
    tree_string += ':'
    tree_string += str(area)
    return tree_string


def area_finder(tree, rotation, boxes):
    """finds the area of the boxes"""
    width = 0
    height = 0
    for box in boxes:
        box.reset_rotate()
    for i in range(len(rotation)):
        if rotation[i] == 1:
            boxes[i].rotate_box()

    w = width_element(tree, boxes)
    if w == -1:
        print('error: width')
    width += int(w)

    h = height_element(tree, boxes)
    if h == -1:
        print('error: height')
    height += int(h)
    area = width * height
    return area


def width_element(node, boxes):
    """part of the algorithm for determining w(p)"""
    if node[0] is '|' or node[0] is '-':
        if node[0] is '-':
            return max(width_element(node[1], boxes), width_element(node[2], boxes))
        elif node[0] is '|':
            return width_element(node[1], boxes) + width_element(node[2], boxes)
    else:
        for i in boxes:
            if node == i.name():
                return i.width()


def height_element(node, boxes):
    """part of the algorithm for determining h(p)"""
    if node[0] is '|' or node[0] is '-':
        if node[0] is '-':
            return height_element(node[1], boxes) + height_element(node[2], boxes)
        elif node[0] is '|':
            return max(height_element(node[1], boxes), height_element(node[2], boxes))
    else:
        for i in boxes:
            if node == i.name():
                return i.height()