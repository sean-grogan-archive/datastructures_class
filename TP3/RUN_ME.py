#!/usr/bin/env python
# encoding: utf-8
"""
TP3.py

Coéquipiers :
Sean Grogan
20001636

solo
"""

from TP3 import main
from TP3_2 import main2
import time
import math

n = input('Number of Leprechauns: ')
t1 = time.time()
print('run 1')
main(int(n), 1)
t2 = time.time()
print('run 2')
main2(int(n), 1)
t3 = time.time()

print('MAIN:  ', math.fabs(t1-t2))
print('MAIN2: ', math.fabs(t3-t2))