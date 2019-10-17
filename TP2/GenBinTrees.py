#!/usr/bin/env python
"""file that has some functions for generating the binary trees"""
__author__ = 'Sean Grogan'

import itertools
from ast import literal_eval


def binary_tree_string(s):
    """imports the list and will output the string that is required for all_binary_trees(s)"""
    strings = []
    strings.append(s[0])
    for i in s[1:]:
        strings += '@'
        strings.append(i)
    return strings


def generate_rotations(num):
    """short function to generate the rotations for the boxes"""
    rotations = []
    for i in range(2**num):
        b = []
        temp = '{:0'+str(num)+'b}'
        for k in str(temp.format(i)):
            b.append(int(k))
        rotations.append(b)
    return rotations


def permutation_boxes(box_keys):
    """permutation the boxes returns a list of a list"""
    return list(itertools.permutations(box_keys))


def all_binary_trees(s):
    """short function to generate binary trees in the from s = 'A@B@C@D@E'"""
    if len(s) == 1:
        yield s
    else:
        for i in range(1, len(s), 2):
            for l in all_binary_trees(s[:i]):
                for r in all_binary_trees(s[i+1:]):
                    yield '({},{},{})'.format(s[i], l, r)


def _string_to_list(string, idx):
    """this function generates the list of binary trees in more list format"""
    def parse_name(string, idx):
        name = ''
        while idx < len(string) and string[idx] not in ',)':
            name += string[idx]
            idx += 1
        return name, idx

    def sanity_check(string, idx):
        # Sanity check: if we don't have a comma or a closing parenthesis here,
        if string[idx] not in ',)':
            raise ValueError('Failed to parse line at character {}.'.format(idx))
        return idx + 1

    result = []
    if string[idx] != '(':
        raise ValueError('Node string not valid at index {}.'.format(idx))
    name, idx = parse_name(string, idx + 1)
    idx = sanity_check(string, idx)
    result.append(name)
    for g in range(2):
        if string[idx] == '(':
            node, idx = _string_to_list(string, idx)
        else:
            node, idx = parse_name(string, idx)
        idx = sanity_check(string, idx)
        result.append(node)
    return tuple(result), idx


def string_to_list(s):
    nodes, length = _string_to_list(s, 0)
    if len(s) != length:
        raise ValueError('string_to_list: did not parse the entire string.')
    return nodes