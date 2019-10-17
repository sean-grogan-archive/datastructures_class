#!/usr/bin/env python
"""this file will generate the binary trees in their cutted form"""

__author__ = 'Sean Grogan'


# (ROOT, LEFT, RIGHT)
# ('@', 'A', ('@', 'B', 'C'))
def binary_tree_seeder(tree_list):
    """seeds the trees with | and -"""
    return_tree = []
    for tree in tree_list:
        horizontal = True
        seeded_tree_1 = node_maker(tree, horizontal)
        # following line can be commented out to reduce solving time
        #seeded_tree_2 = node_maker(tree, not horizontal)

        return_tree.append(seeded_tree_1)
        # following line can be commented out to reduce solving time
        #return_tree.append(seeded_tree_2)

    return return_tree


def node_maker(element, horizontal):
    """seeds the trees with | and -"""
    return_node = []
    # sets the cutting plane
    if horizontal:
        return_node.append('-')
    else:
        return_node.append('|')
    # sets the left child
    if element[1][0] is '@':
        return_node.append(node_maker(element[1], not horizontal))
    else:
        return_node.append(element[1])
    # sets the right child
    if element[2][0] is '@':
        return_node.append(node_maker(element[2], not horizontal))
    else:
        return_node.append(element[2])

    return return_node
