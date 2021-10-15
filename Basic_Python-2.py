"""
Define a function which can generate and print a list
where the values are square of numbers between 1 and 20 (both included).



def square():
    l = []
    for i in range(1, 21):
        l.append(i ** 2)
    return l


print(square())
____________________________________________________________________________________________
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the first 5 elements in the list.

def square():
    l = []
    for i in range(1, 21):
        l.append(i ** 2)
    return l[:5]


print(square())
____________________________________________________________________________________________
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the last 5 elements in the list.

def square():
    l = []
    for i in range(1, 21):
        l.append(i ** 2)
    return l[-5:]


print(square())
_____________________________________________________________________________________________
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print all values except the first 5 elements in the list.

def square():
    l = []
    for i in range(1, 21):
        l.append(i ** 2)
    print(l)
    return l[5:]



print(square())
______________________________________________________________________________________________
Define a function which can generate and
print a tuple where the value are square of numbers between 1 and 20 (both included).

def printtuple():
    l = []
    for i in range(1,21):
        l.append(i ** 2)
    print(l)
    print(tuple(l))

printtuple()
_____________________________________________________________________________________________
With a given tuple (1,2,3,4,5,6,7,8,9,10),
write a program to print the first half values in one line and the last half values in one line.

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t1 = t[:5]
print(t1)
t2 = t[5:]
print(t2)
_______________________________________________________________________________________________
Write a program to generate and print another tuple
whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
l1 = []
for i in t:
    if i % 2 == 0:
        l1.append(i)
print(tuple(l1))
________________________________________________________________________________________________
Write a program which accepts a string as input to print "Yes"
if the string is "yes" or "YES" or "Yes", otherwise print "No".

s = input("Enter the String:")
if s == "yes" or s == "YES" or s == "Yes":
    print("Yes")
else:
    print("No")
_______________________________________________________________________________________________
Write a program which can filter even numbers in a list by using filter function.
The list is: [1,2,3,4,5,6,7,8,9,10].

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = list(filter(lambda x: x % 2 == 0, l))
print(l1)
_______________________________________________________________________________________________
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = list(map(lambda x: x ** x, l))
print(l1)
_____________________________________________________________________________________________________
Write a program which can map() and filter() to make a list whose elements are
square of even number in [1,2,3,4,5,6,7,8,9,10].

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = list(map(lambda x: x ** x, filter(lambda x: x % 2 == 0, l)))
print(l2)
_____________________________________________________________________________________________________
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

l1 = []
for i in range(1, 21):
    l1.append(i)
print(l1)
l2 = list(filter(lambda x: x % 2 == 0, l1))
print(l2)

Method - 2
l2 = list(filter(lambda x: x % 2 == 0, range(1,21)))
print(l2)
_______________________________________________________________________________________________________
Define a class named American which has a static method called printNationality.



class American(object):
    @staticmethod
    def printNationality():
        print("America")


namerica = American
namerica.printNationality()
American.printNationality()
__________________________________________________________________________________________
Define a class named American and its subclass NewYorker.



class American(object):
    pass


class NewYorker(American):
    print("Santosh")


Namerican = American()
Nework = NewYorker()
print(Namerican)
print(Nework)
_____________________________________________________________________________
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.



class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14


a = Circle(2)
print(a.area())
____________________________________________________________________________________
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.



class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


s = Rectangle(12, 2)
print(s.area())
___________________________________________________________________________________________________
"""