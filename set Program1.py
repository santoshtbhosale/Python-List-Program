""""
1.Python Program to Count the Number of Vowels Present in a string using Sets.

s = 'python is very easy language'
s1 = 'aeiou'
s2 = 0
for i in s:
    if i in s1:
        s2 = s2 + 1
print(s2)
_________________________________________________________________________________
2.Reverse a string in Python
________________________________________________________________________________
s = 'python'
s1 = s[::-1]
print(s1)
__________________________________________________________________________________
3.Check if a Python string contains another string
__________________________________________________________________________________

s = 'python is very easy language'
sub = input("Enter the Sub String:")
if sub in s:
    print("The Given Sub String present in main String")
else:
    print("The given Sub String is not Present in main String")

print(s.find('easy'))
_________________________________________________________________________________
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
__________________________________________________________________________________

l = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(str(i))
print(' '.join(l))
__________________________________________________________________________________
Write a program which can compute the factorial of a given numbers.
_________________________________________________________________________________

n = int(input("Enter the number:"))
factorial = 1
if n == 0:
    print("1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(factorial)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


n = int(input("Enter the Number:"))
print(fact(n))
_____________________________________________________________________________________
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is
an integral number between 1 and n (both included). and then the program should print the dictionary.

n = int(input("Enter the number:"))
d = dict()
for i in range(1, n + 1):
    d[i] = i*i
print(d)
____________________________________________________________________________________
Write a program which accepts a sequence of comma-separated numbers from console
and generate a list and a tuple which contains every number.

n = input("Enter the Number:").split(',')
print(n)
print(tuple(n))
____________________________________________________________________________________
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.


class InputOutString(object):
    def __init__(self):
        self.s = " "

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()
______________________________________________________________________________________________
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value
(for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input.
__________________________________________________________________________________________________
import math
D = input("Enter the Number:").split(',')
C = 50
H = 30
item = [i for i in D]
l1 = []
for j in item:
    l1.append(str(round(math.sqrt(2*C*float(j)/H))))
print(','.join(l1))
______________________________________________________________________________________________________
Write a program that accepts a comma separated sequence of words as input and prints
the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

# Method-1
s = 'without,hello,bag,world'.split(',')
items = [x for x in s]
items.sort()
print(','.join(items))
# Method-2
l2 = []
for i in s:
    l2.append(i)
l2.sort()
print(','.join(l2))
____________________________________________________________________________________
Write a program that accepts sequence of lines as input and prints the lines after making
all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

l = input("Enter the word:")
lines = []
while True:
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print(l)
____________________________________________________________________________________________________
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
INPUT:-
hello world and practice makes perfect and hello world again
OUTPUT:-
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

s = 'hello world and practice makes perfect and hello world again'
s1 = []
for i in s.split(" "):
    if i not in s1:
        s1.append(i)
print(' '.join(sorted(set(s1))))
_____________________________________________________________________________________________________
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

b = '0100,0011,1010,1001'
l = []
item = [i for i in b.split(',')]
for j in item:
    s = int(j,2)
    if not s % 5:
        l.append(j)
print(''.join(l))
_____________________________________________________________________________________________

from functools import reduce
l = '11113458911100000111000011000'
l2 = [int(i) for i in l]
print(l2)
l3 = []
for i in l2:
    if i != 0:
        l3.append(i)
for j in l2:
    if j == 0:
        l3.append(j)
print(l3)
square = list(map(lambda x: x * x, l3))
print("Square root of:", square)
add = reduce(lambda x, y: x + y, square)
print("Addition of :", add)
__________________________________________________________________________________________
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

# Method-1
l2 = []
for i in range(1000,3001):
    s = str(i)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
        l2.append(s)
print(','.join(l2))
# Method-2
for i in range(1000,3001):
    p = 0
    for j in str(i):
        if j in ['0','2','4','6','8']:
            p+=1
    if p == 4:
        print(i,end = ',')
________________________________________________________________________________________________
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

s = 'hello world! 123'
letter = 0
digit = 0
for i in s:
    if i.isalpha():
        letter = letter + 1
    elif i.isnumeric():
        digit = digit + 1
print("letter=", letter)
print("digit=", digit)
________________________________________________________________________

"""
