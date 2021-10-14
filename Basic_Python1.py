"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

s = 'Hello world!'
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper = upper + 1
    elif i.islower():
        lower = lower + 1
print("UPPER CASE:",upper)
print("LOWER CASE:",lower)
______________________________________________________________________________
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

n = int(input("Enter the Number:"))
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
n4 = int("%s%s%s%s" % (n, n, n, n))
print(n1 + n2 + n3 + n4)
____________________________________________________________________________________
Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = [i for i in l if i % 2 != 0]
print(l1)
______________________________________________________________________________________
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

t = 0
for i in range(4):
    a = input("Enter the amount:").split()
    value = a[0]
    amount = int(a[1])
    if value == 'D':
        t = t + amount
    elif value == 'W':
        t = t - amount
print("Total Amount is:", t)
________________________________________________________________________________
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

import re

s = 'ABd1234@1,a F1#,2w3E*,2We3345'
value = []
items = [x for x in s.split(',')]
for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass
    if not re.search("[a-z]", p):
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[$#@]", p):
        continue
    elif re.search("\s", p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
______________________________________________________________________________________
You are required to write a program to sort the (name, age, height) tuples by ascending order
where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

from operator import itemgetter
l = []
for i in range(5):
    s = input("Enter the details:")
    l.append(tuple(s.split(",")))
print(sorted(l, key=itemgetter(0, 1, 2)))
_____________________________________________________________________________________________________
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

def generator(num):
    n = 0
    while n < num:
        n = n + 1
        if n % 7 == 0:
            yield n


v = generator(100)
for x in v:
    print(x)
___________________________________________________________________________________
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

s = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'.split()
d = {}
for i in s:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
for j, k in d.items():
    print(j, ":", k)
___________________________________________________________________________________________________
Write a method which can calculate square value of number



def square(n):
    return n ** 2


s = square(5)
print(s)
__________________________________________________________________________________________________
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books.
 But Python has a built-in document function for every built-in functions.

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num):
    '''Return the square value of the input number.

    The input number must be integer.
    '''
    return num ** 2


print(square(2))
print(square.__doc__)
______________________________________________________________________________________
Define a function which can compute the sum of two numbers.



def SumFunction(number1, number2):
    return number1 + number2


print(SumFunction(1, 2))
_____________________________________________________________________________________
Define a function that can convert a integer into a string and print it in console.

def convert(n):
    return str(n)

print(convert(5))
________________________________________________________________________________________
Define a function that can receive two integral numbers in string form and
compute their sum and then print it in console.



def string(s1, s2):
    print(int(s1) + int(s2))


string(11, 12)
________________________________________________________________________________________
Define a function that can accept two strings as input and concatenate them and then print it in console.

def string(s1,s2):
    return s1 + s2

s1 = 'santosh'
s2 = 'bhosale'
print(string(s1,s2))
_________________________________________________________________________________________
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.



def string(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s1) == len(s2):
        print(s1 + s2)
    else:
        print(s2)


s1 = input("Enter the First String:")
s2 = input("Enter the Second String:")
string(s1, s2)
______________________________________________________________________________
Define a function that can accept an integer number as input and print the "It is an even number"
if the number is even, otherwise print "It is an odd number".

def check(num):
    if num % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
check(21)
________________________________________________________________________________________
Define a function which can print a dictionary where the keys are numbers
between 1 and 3 (both included) and the values are square of keys.



def s():
    d = dict()
    for i in range(1, 4):
        d[i] = i ** 2
    print(d)
s()
________________________________________________________________________________________________
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys. The function should just print the values only.

def s():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for j,k in d.items():
        print(k)
s()
"""