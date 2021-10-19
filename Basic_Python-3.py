"""
Define a class named Shape and its subclass Square. The Square class has an init function
which takes a length as argument. Both classes have a area function which can print
the area of the shape where Shape's area is 0 by default.



class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(object):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length

s = Square(3)
print(s.area())
______________________________________________________________________________________
Please raise a RuntimeError exception.

raise RuntimeError('Something Wrong')
____________________________________________________________________________________
Write a function to compute 5/0 and use try/except to catch the exceptions.

def trows():
    return 5/0

try:
    trows()
except ZeroDivisionError:
    print("Division by Zero")
except Exception:
    print("Cuaght an Exception")
finally:
    print("Finally Block")
___________________________________________________________________________________
Write a program which accepts a sequence of words separated by whitespace
as input to print the words composed of digits only.

import re

s = 'ABCD21312434hjdahfjahfj327687467823648'
print(re.findall("\d", s))
_________________________________________________________________________________
Print a unicode string "hello world".

unicodeString = u"hello world!"
print(unicodeString)
__________________________________________________________________________________
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.



____________________________________________________________________________________
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)

n = int(input("Enter the Number:"))
s = 0
for i in range(1, n + 1):
    s = s + (i / (i + 1))
print(s)
________________________________________________________________________________________________
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0)

def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + 100
number = f(5)
print(number)
______________________________________________________________________________
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
number = int(input("Enter the Number:"))
print(f(number))
__________________________________________________________________________________________
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
number = int(input("Enter the Number:"))
values = [str(f(i)) for i in range(1,number+1)]
print(" ".join(values))
______________________________________________________________________
Please write a program using generator to print the even numbers between
0 and n in comma separated form while n is input by User.



def even(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


number = int(input("Enter the n number:"))
l = []
for j in even(number):
    l.append(str(j))
print(",".join(l))
_____________________________________________________________________________
Please write a program using generator to print the numbers
which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

def Print_num(n):
    for i in range(0,n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i
number = int(input("Enter the n Number:"))
l = []
for i in Print_num(number):
    l.append(str(i))
print(",".join(l))
___________________________________________________________________________________________________
Please write assert statements to verify that every number in the list [2,4,6,8] is even.

l = [2, 4, 6, 7]
for i in l:
    assert i % 2 == 0
__________________________________________________________________________________________________
Please write a program which accepts basic mathematic expression from console and print the evaluation result.

n = eval(input("Enter Mathematic expression:"))
print(n)
_____________________________________________________________________________________________________
Please generate a random float where the value is between 10 and 100 using Python math module.

import random
r = random.random()*100
print(r)
______________________________________________________________________________________________________
Please generate a random float where the value is between 5 and 95 using Python math module.

import random
r = random.random()*100-5
print(r)
_____________________________________________________________________________________________________
Please write a program to output a random even number between 0 and 10 inclusive using random module
and list comprehension.

import random
r = random.choice([i for i in range(11) if i % 2 == 0])
print(r)

Input:
DS = [1111, 8888, 3333, 2222]
Model = {"M1": [0, 1, 2, 3], "M2": [1, 3], "M3": [0, 2]}
Output:
M1-Batch=[1111,8888,3333,2222]
M2-Batch=[8888,2222]
M3-Batch=[1111,3333]

l = [1111, 8888, 3333, 2222]
m = {"M1": [0, 1, 2, 3], "M2": [1, 3], "M3": [0, 2]}
l1 = [i for i in m.values()]
l4 = [j for j in l1[0]]
l4[0] = l[0]
l4[1] = l[1]
l4[2] = l[2]
l4[3] = l[3]
print("M1 Batch=", l4)
l5 = [j for j in l1[1]]
l5[0] = l[1]
l5[1] = l[3]
print("M2 Batch=", l5)
l6 = [j for j in l1[2]]
l6[0] = l[0]
l6[1] = l[2]
print("M2 Batch=", l5)

import numpy as np

DS = [1111, 8888, 3333, 2222]
Model = {"M1": [0, 1, 2, 3], "M2": [1, 3], "M3": [0, 2]}
ds_array = np.array(DS)
for i in Model:
    index_m = np.array(Model[i])
    print(ds_array[index_m])
_______________________________________________________________________________________
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

import random

s = random.sample(range(100, 201), 5)
print(s)
__________________________________________________________________________________________
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

import random
s = random.sample([i for i in range(100, 201) if i % 2 == 0],5)
print(s)
"""
