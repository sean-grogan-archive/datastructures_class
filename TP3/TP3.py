#!/usr/bin/env python
# encoding: utf-8
"""
TP3.py

Coéquipiers :
Sean Grogan
20001636

solo
"""

__author__ = 'Sean Grogan'

from SortedListMap import SortedListMap
from TreeMap import TreeMap
import random
import math
import time


def main(number_of_leprechauns, seed=None):
    start = time.time()
    #initializaton of vars
    n = number_of_leprechauns
    random.seed(seed)
    gold_leprechaun = SortedListMap()
    location_leprechaun = SortedListMap()
    def_gold = 1000000

    if n <= 2:
        print("pas assez de Leprechauns entres.")
        print("s'il vous plaît donner plus de 2 Leprechauns.")
    else:
        # creates a sorted map list of leprechauns
        for i in range(n):
            gold_leprechaun[i] = def_gold
            location_leprechaun[i+1] = i

        while len(gold_leprechaun) > 2:
            for l in location_leprechaun:
                old_loc = location_leprechaun[l]
                lep_id = l

                r = random.uniform(-1, 1)
                new_loc = int(old_loc + r * gold_leprechaun[old_loc])

                location_leprechaun[lep_id] = new_loc
                gold_value = gold_leprechaun[old_loc]
                del(gold_leprechaun[old_loc])
                gold_leprechaun[new_loc] = gold_value
                close = gold_leprechaun.find_close(new_loc)

                stolen = math.ceil(gold_leprechaun[close]/2)
                gold_leprechaun[close] -= stolen
                gold_leprechaun[new_loc] += stolen

                if gold_leprechaun[close] <= 0:
                    loc_del = None
                    for i in location_leprechaun:
                        if location_leprechaun[i] == close:
                            loc_del = i
                    print('Le leprechaun', loc_del, 'disparait! Il reste ', len(location_leprechaun)-1, 'leprechauns')
                    del(gold_leprechaun[close])
                    del(location_leprechaun[loc_del])
                if len(location_leprechaun) <= 2:
                    # ensures that the loop breaks before another leprechaun steals gold
                    break

        print('')
        # print('----------------------------------------------------------------')
        # print('Deux Leprechauns restent!')
        res = []
        for i in location_leprechaun:
            res.append(i)
        print('Les 2 gagnants sont les leprechauns ', res[0], ' et ', res[1])
        print(math.fabs(start-time.time()), 'seconds')
        print('')
        return res
