"""
1.Python Program to find the Union of two Lists.

l = [10,20,20]
l1 = [10,20,30,30]
l2 = set(l).union(set(l1))
print(list(l2))

l3 = []
for i in l:
    if i not in l3:
        l3.append(i)
for i in l1:
    if i not in l3:
        l3.append(i)
print(l3)
________________________________________________________________________________
2.write a Program to find the intersection of two Lists.

# Method-1
l = [10, 20, 20]
l1 = [10, 20, 30, 30]
l3 = set(l).intersection(set(l1))
print(list(l3))
# Method-2
l4 = []
for i in l:
    if i in l1:
        l4.append(i)
print(list(set(l4)))
________________________________________________________________________________
3.Python Program to create a List of Tuples with the First Element as the Number and Second Element
as the Square of the Number.

# Method - 1
n = int(input("Enter the Number:"))
for i in range(1, n + 1):
    print((i, i ** 2))
# Method - 2
l = [(i, i ** 2) for i in range(1, n + 1)]
print(l)
___________________________________________________________________________________
4. Python Program to find all Numbers in a Range which are Perfect Squares and
sum of all Digits in the Number is less than 10.

n = int(input("Enter the Number:"))
for i in range(1, n + 1):
    if (i ** 0.5) ** 2 == i and sum(list(map(int, str(i)))) < 10:
        print(i, end=",")
___________________________________________________________________________________
5.Python Program to Find the Cumulative Sum of a List where the i th element is the sum of the
First i + 1 Elements from the original list.

# Method -3
l = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(l)):
    print(sum(l[0:i + 1]),end=" ")

# Method-2
l1 = [sum(l[0:i + 1])for i in range(len(l))]
print(l1)
_____________________________________________________________________________________
6.Python Program to Generate Random Numbers from 1 to 20 and append Them to the List.

from random import *
l1 = []
for i in range(10):
    s = randint(1, 20)
    l1.append(s)
print(l1)
________________________________________________________________________________________
7.Python Program to sort a List of Tuples in increasing Order by the Last Elements in Each Tuple.



def last(n):
    return n[-1]


def sort(tuples):
    return sorted(tuples, key=last)


print(sort([(1, 4), (3, 8), (2, 6), (4, 0), (8, 5)]))
_______________________________________________________________________________________
8.Python Program to Swap the First and Last Value of a list.

# Method-1
l = [10, 22, 33, 44, 55]
l[-1], l[0] = l[0], l[-1]
print(l)

l = [10, 22, 33, 44, 55]
l1 = len(l)
temp = l[0]
l[0] = l[l1-1]
l[l1-1] = temp
print(l)

l = [10, 22, 33, 44, 55]
t = l[-1],l[0]
l[0],l[-1] = t
print(l)
__________________________________________________________________________
9.Python Program to remove the duplicate items from a List.

l = ['Red', 'Blue', 'Yellow', 'Red', 'White', 'Red']
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
_________________________________________________________________________
10.Python Program to Read a List of Words and Return the length of the Longest One.

l = ['Red', 'Blue', 'Yellow', 'Red', 'White', 'Red']
l2 = sorted(l, key=len)
print(l2[-1])
___________________________________________________________________________
11.Python program to remove the ith Occurrence of the Given Word in a list
where Words can Repeat.

l = ['Red', 'Blue', 'Yellow', 'Red', 'Yellow', 'Red']
n = int(input("Enter the number:"))
l1 = []
for i in l:
    if i == l[n]:
        continue
    l1.append(i)
print(l1)
___________________________________________________________________________
12.Python Program to Remove All Tuples in a List of Tuples.

l = [11, 23, (), 21, (), 23, (), (), 20]
l1 = []
for i in l:
    if i == ():
        continue
    l1.append(i)
print(l1)
___________________________________________________________________________
13. Python program to find Element Occurring odd Number of Times in a List.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = 0
for i in l:
    if i % 2 != 0:
        l1 = l1 + 1
print(l1)
___________________________________________________________________________
14.Write a Python Program to flatten a shallow list.

import itertools
l = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 4]]
l1 = list(itertools.chain(*l))
print(l1)

l = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 4]]
l1 = []
for i in l:
    for j in i:
        l1.append(j)
print(l1)
__________________________________________________________________________
15.Write a Python program to append a list to the second list.

l = [1, 2, 3, 4]
l1 = ['Red', 'Blue', 'White']
l2 = l + l1
print(l2)

l = [1, 2, 3, 4]
l1 = ['Red', 'Blue', 'White']
l2 = []
for i in l:
    l2.append(i)
for i in l1:
    l2.append(i)
print(l2)
__________________________________________________________________________
16.Write a Python Program to select an item randomly from a list.

import random
l = [10, 22, 11, 34, 23, 44, 56, 78, 88]
print(random.choice(l))
___________________________________________________________________________
17.Write a Python Program to check whether two lists are circularly identical.
Write a Python Program to check whether the given number in a list is anagram or not.

l = [10, 10, 0, 0, 10]
l1 = [10, 10, 10, 0, 1]
l2 = ''.join(map(str, l1)) in ''.join(map(str, l * 2))
print(l2)
__________________________________________________________________________
18.Write a Python Program to check whether the given string is anagram or not.

s = 'python'
s1 = 'thonpn'
s2 = ''.join(map(str, s1)) in ''.join(map(str, s * 2))
print(s2)
___________________________________________________________________________
19.Write a Python program to find the second largest number in a list.

l = [10, 11, 22, 34, 44, 56, 77, 35, 89, 90]
l.sort()
print(l[-2])

l = [10, 11, 22, 34, 44, 56, 77, 35, 89, 90]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(sorted(l1))
print(l1[-2])
_________________________________________________________________________________
20.Write a python program to find second smallest number in a list.
"""
l = [10, 11, 22, 22, 34, 44, 56, 56, 77, 35, 89, 90]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(sorted(l1))
print(l1[1])
