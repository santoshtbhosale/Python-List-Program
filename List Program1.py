"""
Write a Python Program to get unique values from a list.

l1 = [10, 11, 12, 11, 13, 14, 12, 11, 10]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
________________________________________________________________________
Write a python program to get the frequency of the elements in a list.

import collections
from collections import Counter
l1 = [10, 11, 12, 11, 13, 14, 12, 11, 10]
s = collections.Counter(l1)
print(s)
"""
l1 = [10, 11, 12, 11, 13, 14, 12, 11, 10]
d = {}
for i in l1:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
for j,k in d.items():
    print(j,":",k)


