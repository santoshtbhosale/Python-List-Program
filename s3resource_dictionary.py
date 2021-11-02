'''
1) Python: Sort (ascending and descending) a dictionary by value
Method - 1
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(d)
d1 = sorted((v, k) for (k, v) in d.items())
print(d1)
Method-2
for i in sorted(d, key=d.get, reverse=False):
    print(i, d[i], end=" ")
Method-3
from collections import Counter
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(d)
d1 = Counter(d)
print(d1)
print(d1.most_common())
print(d1.most_common()[::-1])
_________________________________________________________________________________
Write a Python script to add a key to a dictionary. Go to the editor
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

d = {0: 10, 1: 20}
d[2] = '30'
print(d)
d.setdefault(2, 30)
print(d)
________________________________________________________________________________________
Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}
d4 = {}
print(d4)
for i in (d1,d2,d3):
    d4.update(i)
print(d4)
___________________________________________________________________________________________________________
Add a Key-Vale Pair to the Dictionary

d = {}
d.update({'a':100})
d.setdefault('b',200)
d['c'] = 300
print(d)
__________________________________________________________________________________________________________
Concatenate Two Dictionary into One

d1 = {'A': 1, 'B': 2}
d2 = {'C': 3}
d1.update(d2)
print(d1)
_________________________________________________________________________________________________________
to Check if a given key Exist in a Dictionary or Not

d = {'A': 1, 'B': 2, 'C': 3}
n = input("Enter the Key:")
if n in d.keys():
    print("given key Exist in a Dictionary")
else:
    print("given key Does not Exist in a Dictionary")
_____________________________________________________________________________________________________
To generate a Dictionary that Contains Numbers(between 1 and n) in the form (x.x*x)

n = int(input('Enter the Number:'))
d = {x: x * x for x in range(1, n + 1)}
print(d)
____________________________________________________________________________________________________
To Sum of All the items in a Dictionary

d = {'A': 100, 'B': 200, 'C': 300}
print(sum(d.values()))
__________________________________________________________________________________________________
To Multiply All the Items in a Dictionary

mul = 1
d = {'A': 100, 'B': 200, 'C': 300}
for i in d.values():
    mul = mul * i
print(mul)
________________________________________________________________________________________________
To Remove the Given Key from a Dictionary

d = {'A': 100, 'B': 200, 'C': 300}
del d['A']
print(d)
_________________________________________________________________________________________________
To form a Dictionary from an Object of a class

class A(object):
    def __init__(self):
        self.A = 1
        self.B = 2
s = A()
print(s.__dict__)
_____________________________________________________________________________________________
To Map Two Lists into a Dictionary

l = [1, 2, 3, 4, 5, 7]
l1 = [7, 4, 2, 3, 7]
d = dict(zip(l, l1))
print(d)
_____________________________________________________________________________________________
To Count the frequency of words Apperaring in a String using Dictionary.

# Method -1
s = 'Python is very easy Language Python'.split()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
for k, v in d.items():
    print(k, ":", v)
# Method-2
l = []
l1 = [s.count(i) for i in s]
print(dict(zip(s, l1)))
__________________________________________________________________________________________________
To Create a Dictionary with key as First Character and Value as Words Starting with that Character.

s = 'Python is very easy Language'
s1 = s.split()
d = {}
for i in s1:
    d[i[0]] = []
    d[i[0]].append(i)
for k, v in d.items():
    print(k, ":", v)
____________________________________________________________________________________________________
Write Python Program to remove a key from a dictionary

d = {'A': 100, 'B': 200, 'C': 267, 'D': 300}
if 'A' in d:
    del d['A']
print(d)
___________________________________________________________________________________________________
Sort a dictionary by key

d = {'Red': 100, 'Blue': 200, 'White': 300, 'Yellow': 400}

for i in sorted(d):
    print(i, ":", d[i])
______________________________________________________________________________________________________
To get the Maximum and Minimum value in a Dictionary

d = {'Red': 100, 'Blue': 200, 'White': 300, 'Yellow': 400}
d1 = max(d.values())
d2 = min(d.values())
print("Maximum Value is:",d1)
print("Minimum Value is:",d2)
_____________________________________________________________________________________________________
To get a dictionary from an object fields

class A(object):
    def __init__(self):
        self.a = 'red'
        self.b = 'blue'
        self.c = 'yellow'
s = A()
print(s.__dict__)
_________________________________________________________________________________________________
To remove duplicates from dictionary.

d = {'A': 100, 'B': 200, 'C': 267, 'D': 300, 'E': 200}
d1 = {}
for k,v in d.items():
    if v not in d1.values():
        d1[k] = v
print(d1)
________________________________________________________________________________________________
To check a dictionary is empty or not

d = eval(input("Enter the Dictionary:"))
if d == {}:
    print("The Given Dictionary is empty")
else:
    print("The Given Dictionary is not empty")
________________________________________________________________________________________________
To Combine two dictionary adding values for common keys

from collections import Counter
d1 = {'A': 100, 'B': 200, 'C': 267, 'D': 300, 'E': 200}
d2 = {'A': 100, 'B': 300, 'C': 200, 'D': 300, 'E': 300}
d = Counter(d1) + Counter(d2)
print(d)
__________________________________________________________________________________________________
To Print all unique values in a dictionary

Method-1

d = {'A': 100, 'B': 200, 'C': 267, 'D': 300, 'E': 200}
l = []
for i in d.values():
    if i in l:
        continue
    else:
        l.append(i)
print(l)
_________________________________________________________________________________________________
To Create and display all combination of letters, selecting each letter from a different key in a dictionary.

import itertools

d = {'1': ['a', 'b'], '2': ['c', 'd']}
d1 = list(itertools.product(d.values()))
print(d1)
_________________________________________________________________________________________________________________
To find the Highest 3 Value in a dictionary

d = {'A': 100, 'B': 200, 'C': 267, 'D': 300, 'E': 200}
l = []
for i in d.values():
    l.append(i)

print(sorted(l)[-3:])

s = 'santosh'
k = int(input("Enter the position number"))
s1 = ''
for i in s:
    s1 = s1 + chr(ord(i)+k)
print(s1)

'''

