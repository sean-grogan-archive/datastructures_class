__author__ = 'Sean Grogan'
#--------------------------------------------------------------------------------------------------
# A simple toolbox for me to do some scratch work in
#--------------------------------------------------------------------------------------------------
from ast import literal_eval
import sys

"""
def wub_wub_string_to_list(tree_list):
    new_list = []

    for item in tree_list:
        tmp = ""
        for char in item:
            if char not in ['(',')',',']:
                tmp+="'{}'".format(char)
            else:
                tmp+=char
        new_list.append(tmp)

    new_list = [literal_eval(i) for i in new_list]
    return new_list

tree_list = ['(@,A,(@,B,C))', '(@,(@,A,B),C)', '(@,A,(@,C,B))', '(@,(@,A,C),B)',
            '(@,B,(@,A,C))', '(@,(@,B,A),C)', '(@,B,(@,C,A))', '(@,(@,B,C),A)',
            '(@,C,(@,A,B))', '(@,(@,C,A),B)', '(@,C,(@,B,A))', '(@,(@,C,B),A)']

new_list = wub_wub_string_to_list(tree_list)

print(new_list)
print(new_list[0])
print(new_list[0][0])
print(new_list[0][1])
print(new_list[0][2])
"""

'''
def string_to_list(string):
    return_list = []
    word = ''
    c = 0
    while c <= len(string):
        if string[c] in '([{':
            index = c + 1
            return_list.append(string_to_list(string[index:]))
            c = string.index(')', index)
        elif string[c] is ',':
            return_list.append(word)
            word = ''
        elif string[c] in ')]}':
            return return_list
        else:
            word = word + string[c]
        c += 1

jack = '(@,(@,FF,(@,(@,EE,DD),A)),(@,C,B))'
print(jack)
print(list(string_to_list(jack)))

def allbinarytrees(s):
    if len(s) == 1:
        yield s
    else:
        for i in range(1, len(s), 2):
            for l in allbinarytrees(s[:i]):
                for r in allbinarytrees(s[i+1:]):
                    yield '({},{},{})'.format(s[i], l, r)

#for t in allbinarytrees('A@B@C@D@E'):
#    jack.append(t)
#    print(t)

#print(jack)
'''

def _string_to_list(s, idx):
    def parse_name(s, idx):
        name = ''
        # A name goes until a comma or a closing parenthesis.
        # XXX: Maybe change this to accept only letters, and avoid going through
        #      opening parenthesis with a missing comma for example.
        while idx < len(s) and s[idx] not in ',)':
            name += s[idx]
            idx += 1
        return name, idx
    def sanity_check(s, idx):
        # Sanity check: if we don't have a comma or a closing parenthesis here,
        # our parsing failed.
        if s[idx] not in ',)':
            raise ValueError('Failed to parse line at character {}.'.format(idx))
        # Else we skip that token.
        return idx + 1
    result = []
    if s[idx] != '(':
        raise ValueError('Node string not valid at index {}.'.format(idx))
    # Parse the content of the node.
    name, idx = parse_name(s, idx + 1)
    # Don't forget to do a sanity check after parsing that part!
    idx = sanity_check(s, idx)
    # Add the node name in the resulting list.
    result.append(name)
    # Now parsing left and right node.
    for _ in range(2):
        if s[idx] == '(':
            # If we start with an opening parenthesis, we want to parse the
            # new sub-node.
            node, idx = _string_to_list(s, idx)
        else:
            # Else we should just have a simple name, parse it.
            node, idx = parse_name(s, idx)
        # Sanity check!
        idx = sanity_check(s, idx)
        # Don't forget to add the node to the result!
        result.append(node)
    # We return both the resulting node and the index after the closing
    # parenthesis, which permits the recursion to work and skip the sub-nodes
    # (skip the whole sub-node, to continue in its own node.
    return tuple(result), idx


def string_to_list(s):
    nodes, length = _string_to_list(s, 0)
    if len(s) != length:
        raise ValueError('string_to_list: did not parse the entire string.')
    return nodes

if __name__ == '__main__':
    #if len(sys.argv) < 2:
    #    sys.exit('usage: {} tree-string'.format(sys.argv[0]))
    jack = '(@,(@,FF,(@,(@,EE,DD),A)),(@,C,B))'
    print(jack)
    print(string_to_list(jack))