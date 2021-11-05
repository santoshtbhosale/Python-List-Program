'''
Write a Python function that takes a list of words and return the longest word and
the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9

s = ['python', 'is', 'very', 'easy', 'language', 'i', 'like', 'these', 'type', 'of', 'system']

l = []

for i in s:
    l.append((len(i),i))
    l.sort()

print("Longest word:",l[-1][1])
print("Length of the longest word:",l[-1][0])
_______________________________________________________________________________________________________

Write a Python program to remove the nth index character from a nonempty string.

s = 'python'
n = int(input("Enter the N number character:"))
s1 = s[:n] + s[n+1:]
print(s1)
_________________________________________________________________________________________________________
Write a Python program to change a given string to a new string
where the first and last chars have been exchanged.

s = 'python'
s1 = ''
for i in s:
    s1 = s1 + i
print(s1[-1] + s1[1:-1] + s1[0])
_______________________________________________________________________________________________________
 Write a Python program to remove the characters which have odd index values of a given string.

str = 'python'
result = ""
for i in range(len(str)):
    if i % 2 == 0:
        result = result + str[i]
print(result)
______________________________________________________________________________________________________
Write a Python program to count the occurrences of each word in a given sentence.

s = 'The python is very easy very the python easy'
d = dict()
s1 = s.split()
for i in s1:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
_________________________________________________________________________________________________________
Write a Python program that accepts a comma separated sequence of words as input and
prints the unique words in sorted form (alphanumerically). Go to the editor
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red

s = 'red, white, black, red, green'
s1 = s.split()
s2 = sorted(set(s1))
print(*s2)
l1 = [i for i in s1]
print(*sorted(set(l1)))
_______________________________________________________________________________________________________
Write a Python function to insert a string in the middle of a string.

s = 'python'
word = '[[]]'
s3 = word[:2] + s + word[2:]
print(s3)
_____________________________________________________________________________________________________
Write a Python function to get a string made of 4 copies of the last two
characters of a specified string (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses

s = 'python'
if len(s) >= 2:
    s1 = s[-2:] * 4
    print(s1)
else:
    print("String Length is required minimum 2 Character")
______________________________________________________________________________________________________




def string(s):
    if len(s) >= 2:
        s1 = s[-2:] * 4
        print(s1)
    else:
        print("String Length is required minimum 2 Character")


string('python')
_____________________________________________________________________________________________________
Write a Python function to get a string made of its first three characters of a specified string.
If the length of the string is less than 3 then return the original string. Go to the editor
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt

s = input("Enter the String:")
if len(s) >= 3:
    s1 = s[:3]
    print(s1)
else:
    print(s)
____________________________________________________________________________________________________
Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python

s = 'https://www.w3resource.com/python-exercises'
print(*s.rsplit('/',1))
print(s.rsplit('-',1)[0])
__________________________________________________________________________________________________
 Write a Python function to reverses a string if it's length is a multiple of 4.

s = input("Enter the String:")
if len(s) % 4 == 0:
    print("".join(reversed(s)))
else:
    print(s)
___________________________________________________________________________________________________
Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters.

s = 'python'
add = 0
for i in s[:4]:
    if i.upper() == i:
        add = add + 1
if add >= 2:
    print(s.upper())
else:
    print("In a String No any Character has Alphabets")
____________________________________________________________________________________________________
Write a Python program to sort a string lexicographically.

s = 'W3RESOURCE'
s1 = sorted(s,key=str)
print(s1)
_____________________________________________________________________________________________________
Write a Python program to create a Caesar encryption.

s = input("Enter the Word:")
k = int(input("Enter the k position of Character:"))
s1 = " "
for i in s:
    s1 = s1 + chr(ord(i) + k)
print(s1)
__________________________________________________________________________________________________
x = 22
print(""+"{:10d}".format(x))
print(""+"{:<10d}".format(x))
print(""+"{:^10d}".format(x))
____________________________________________________________________________________________________
Write a Python program to count occurrences of a substring in a string.

s = 'python is very easy is language'
sub = 'is'
add = 0
for i in s.split():
    if sub in i:
        add = add + 1
print(add)
__________________________________________________________________________________________________
Write a Python program to reverse words in a string.

s = 'python is very easy is language'.split()
s1 =[]
for i in s[::-1]:
    s1.append(i)
print(" ".join(s1))
_________________________________________________________________________________________________
Write a Python program to strip a set of characters from a string.

s = 'python is very easy is language'
s1 = 'aeiou'
s2 =''
for i in s:
    if i not in s1:
        s2 = s2 + i
print(s2)
_________________________________________________________________________________________________
Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2

s = 'thequickbrownfoxjumpsoverthelazydog'
d = {}
for i in s:
    d[i] = d.get(i,0) + 1
for j, k in d.items():
    if d[j] > 1:
        print(j, ":", k)
__________________________________________________________________________________________________________
Write a Python program to print the index of the character in a string.
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9

s = 'w3resource'
i = 0
for j in s:
    print("Current character", j, "position at", i)
    i = i + 1
_________________________________________________________________________________________________________
Write a Python program to check whether a string contains all letters of the alphabet.

s = 'abcdefghijklmnopqrstuvwxz'
s1 ='abcdefghijklmnopqrstuvwxyz'
if s in s1:
    print("True")
else:
    print("False")
_________________________________________________________________________________________________________
Write a Python program to convert a given string into a list of words.

s = 'python is very easy language'
s1 = s.split()
print(s1)
_______________________________________________________________________________________________________
Write a Python program to lowercase first n characters in a string

s = input("Enter the String:")
n = int(input("Enter the n Characters:"))
s1 = s[:n].lower() + s[n:]
print(s1)
________________________________________________________________________________________________________
Write a Python program to swap comma and dot in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"

s = '32.054,23'
s1 = s.replace('.', '-').replace(',', '.').replace('-', ',')
print(s1)
_________________________________________________________________________________________________________
Write a Python program to count and display the vowels of a given text.

s = 'python is very easy language'
s1 = 'aeiou'
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
for j, k in d.items():
    if j in s1:
        print(j, ":", k)

s = 'python is very easy language'
s1 = 'aeiou'
print(len([i for i in s if i in s1]))
print([i for i in s if i in s1])
_________________________________________________________________________________________________________
 Write a Python program to split a string on the last occurrence of the delimiter.

str1 = "w,3,r,e,s,o,u,r,c,e"
print(str1.rsplit(',',3))
________________________________________________________________________________________________________
Write a Python program to find the first non-repeating character in given string.

s = 'abcabcdefde'
s1 = []
d = {}
for i in s:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
        s1.append(i)
for i in s1:
    if d[i] == 1:
        print(i)
____________________________________________________________________________________________________
Write a Python program to print all permutations with given repetition number of characters of a given string.

s = 'python'
s1 = len(s)
for i in range(s1):
    for j in range(s1):
        for k in range(s1):
            for l in range(s1):
                for m in range(s1):
                    for n in range(s1):
                        if i != j and j != k and k != l and l != m and m != n and i != n:
                            print(s[i], s[j], s[k], s[l], s[m], s[n])
_________________________________________________________________________________________________________
Write a Python program to find the first repeated character in a given string.

s = 'abcdabcd'
for i, c in enumerate(s):
    if s[:i + 1].count(c) > 1:
        print(c)
________________________________________________________________________________________________________
Write a Python program to find the first repeated character of a given string
where the index of first occurrence is smallest.

s = 'abcdabcd'
d = {}
for i in s:
    if i in d:
        print(i,s.index(i))
    else:
        d[i] = 0
________________________________________________________________________________________________________
Write a Python program to find the first repeated word in a given string.

s = 'ab bc ab bd bc'
s1 = set(s)
for i in s.split():
    if i in s1:
        print(i)
    else:
        s1.add(i)
_______________________________________________________________________________________________________
Write a Python program to move spaces to the front of a given string.

s = "python is"
s1 = s.replace(' ','')

s1 = " " + s1
print(s1)
______________________________________________________________________________________________________
Write a Python program to find the maximum occurring character in a given string.

s = 'is very vervv easy'
d = {}
for i in s:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
r = max(d, key=d.get)
print(r)
_______________________________________________________________________________________________________
Write a Python program to capitalize first and last letters of each word of a given string.

s = 'python is very easy'
s2 = s.title()
print(s2)
result = ""
for i in s2.split():
    result = result + i[:-1] + i[-1].upper() + ' '
print(result)
_________________________________________________________________________________________________________
Write a Python program to remove duplicate characters of a given string.

s = 'geeksforgeeks'
d = set(s)
print("".join(d))
f = ""
for i in s:
    if i in f:
        pass
    else:
        f = f + i
print(f)
__________________________________________________________________________________________________________


from collections import OrderedDict
s = {'name','age','gender','age'}
d = OrderedDict.fromkeys(s)
print(d)
d = OrderedDict.fromkeys(s,10)
print(d)
________________________________________________________________________________________________________
Write a Python program to compute sum of digits of a given string.

s = '123python3526'
s1 = 0
for i in s:
    if i.isdigit():
        s1 = s1 + int(i)
print(s1)
_________________________________________________________________________________________________________
Write a Python program to remove leading zeros from an IP address.

s = '255.0.0.09'
s2 = ".".join([str(int(i)) for i in s.split('.')])
print(s2)
_______________________________________________________________________________________________________
Write a Python program to find maximum length of consecutive 0’s in a given binary string.

s ='111000001111000011000'
s1 = max(map(len,s.split('1')))
print(s1)
_______________________________________________________________________________________________________
 Write a Python program to find all the common characters in lexicographical order from two given lower case strings.
 If there are no common letters print "No common characters".

 Python code to print common characters of two Strings in alphabetical order.

s = 'adefeb'
s1 = 'abce'
d = set(s)
d1 = set(s1)
d3 = d.intersection(d1)
if not d3:
    print("No common characters")
else:
    print(*sorted(d3))

from collections import Counter
s = 'adefeb'
s1 = 'abce'
d1 = Counter(s)
print(d1)
d2 = Counter(s1)
d3 = d1 & d2
print(d3)
if len(d3) == 0:
    print("No common Characters")

c = list(d3.elements())
print(c)
c = sorted(c)
print(c)
________________________________________________________________________________________
Write a Python program to create two strings from a given string.
Create the first string using those character which occurs only once and
create the second string which consists of multi-time occurring characters in the said string.

from collections import Counter

s = "aabbcceffgh"
str_char_ctr = Counter(s)
part1 = [key for (key, count) in str_char_ctr.items() if count == 1]
part2 = [key for (key, count) in str_char_ctr.items() if count > 1]
part1.sort()
part2.sort()
print(''.join(part1))
print(''.join(part2))
______________________________________________________________________________________________
Write a Python program to find the longest sub-string from two given strings

s = 'python is very easy language'
s1 = 'geeks for geeksre are very easy'
sub1 = 'easy'
sub2 = 'easy'
s2 = ''
for i in s.split():
    if i in sub1:
        s2 = s2 + i + " "
for j in s1.split():
    if j in sub2:
        s2 = s2 + j + " "
print("".join(s2))
print(max(s2.split()))
__________________________________________________________________________________________________
 Write a Python program to create a string from two given strings concatenating
 uncommon characters of the said strings.

s = 'python is very easy'
s1 = 'python are very difficult'
s2 = ''
for i in s.split():
    if i not in s1:
        s2 = s2 + i + ' '
for j in s1.split():
    if j not in s:
        s2 = s2 + j + ' '
print(s2)
_________________________________________________________________________________________________
Write a Python program to move all spaces to the front of a given string in single traversal

s = 'python is very easy'
s1 = ''
for i in s.split():
    s1 = ' ' + s1 + i
print(s1)
__________________________________________________________________________________________________
Write a Python code to remove all characters except a specified character in a given string.
Original string
Python Exercises
Remove all characters except P in the said string:
P

s = 'Python ExerPcises'
#s1 = list(s)
#print("Remove all characters except P in the said string:","".join(s1[:1]))
s1 = 'P'
for i in s:
    if i == s1:
        print(i,end=" ")
_________________________________________________________________________________________________
Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.

s = 'PYTthon2368487jhjdfjgGHGDSHDGH@#$%@^'
s1, s2, s3, s5 = 0, 0, 0, 0
s4 = '!@#$%^&*'
for i in s:
    if i.islower():
        s1 = s1 + 1
    elif i.isupper():
        s2 = s2 + 1
    elif i.isnumeric():
        s3 = s3 + 1
    elif i in s4:
        s5 = s5 + 1
print("Lowercase Count:", s1)
print("Uppercase Count:", s2)
print("Numeric Values Count:", s3)
print("special character Count:", s5)
_______________________________________________________________________________________________________________
Write a Python program to find the minimum window in a given string which will contain all
the characters of another given string.

Example 1
Input
str1 = " PRWSOERIUSFK "
str2 = " OSU "
Output:
Minimum window is "OERIUS"

s1 = " PRWSOERIUSFK "
s2 = " OSU "
for i in s1:
    if i in s2:
        print(i,end=" ")
_____________________________________________________________________________________________
Write a Python program to count number of non-empty substrings of a given string.
formula-n * (n + 1)/2

s = 'python'
s1 = len(s)
print(int(s1 * (s1 + 1)/2))
______________________________________________________________________________________________
Write a Python program to count characters at
same position in a given string (lower and uppercase characters) as in English alphabet.

s = 'adedf'
s1 = 0
for i in range(len(s)):
    if (i == ord(s[i]) - ord('A')) or (i == ord(s[i]) - ord('a')):
        s1 = s1 + 1
print(s1)
_________________________________________________________________________________________________
Write a Python program to find smallest and largest word in a given string.

s = 'python is very easy language'
s2 = []
for i in s.split():
    s2.append((len(i), i))
print(*max(s2))
print(*min(s2))
_____________________________________________________________________________________________________
Write a Python program to count number of substrings with same first and last characters of a given string.

s = 'pythonp'
s1 = len(s)
s2 = 0
for i in range(s1):
    for j in range(i,s1):
        if s[i] == s[j]:
            s2 = s2 + 1
print(s2)
_________________________________________________________________________________________________________
Write a Python program to find the index of a given string at which a given substring starts.
If the substring is not found in the given string return 'Not found'.

s = 'python language'
sub = 'ng'
if len(sub) > len(s):
    print('Not Found')
for i in range(len(s)):
    for j in range(len(sub)):
        if s[i + j] == sub[j] and j == len(sub) - 1:
            print(i)
        elif s[i + j] != sub[j]:
            break
______________________________________________________________________________________________________
Write a Python program to wrap a given string into a paragraph of given width. Go to the editor
Sample Output:
Input a string: The quick brown fox.
Input the width of the paragraph: 10
Result:
The quick
brown fox.
_______________________________________________________________________________________________________
Write a Python program to print four values decimal, octal,
hexadecimal (capitalized), binary in a single line of a given integer.

n = int(input("Enter the integer number:"))
o = oct(n)[2:]
h = hex(n)[2:]
b = bin(n)[2:]
d = n
print(o, h, b, d)
____________________________________________________________________________________________________
Write a Python program to swap cases of a given string. Go to the editor
Sample Output:
pYTHON eXERCISES
jAVA
nUMpY

s = 'Python Exercises'
s1 = s.swapcase()
print(s1)
s2 =""
for i in s:
    if i.isupper():
        s2 = s2 + i.lower()
    else:
        s2 = s2 + i.upper()
print(s2)
___________________________________________________________________________________________________
Write a Python program to convert a given Bytearray to Hexadecimal string.
Sample Output:
Original Bytearray :
[111, 12, 45, 67, 109]
Hexadecimal string:
6f0c2d436d

l = [111, 12, 45, 67, 109]

for i in l:
    #print(hex(i)[2:],end="")
    print(("".join('{:02x}'.format(i))))
_________________________________________________________________________________
Write a Python program to delete all occurrences of a specified character in a given string.
Sample Output:
Original string:
Delete all occurrences of a specified character in a given string
Modified string:
Delete ll occurrences of specified chrcter in given string

s = 'Delete all occurrences of a specified character in a given string'
s1 = s.replace('a', '')
print(s1)
_____________________________________________________________________________________________
Write a Python program find the common values that appear in two given strings. Go to the editor
Sample Output:
Original strings:
Python3
Python2.7
Intersection of two said String:
Python

s = 'Python3'
s1 = 'Python2.7'
s2 =''
for i in s:
    if i in s1:
        s2 = s2 + i
print(s2)
__________________________________________________________________________________________________
Write a Python program to check whether a given string contains a capital letter,
a lower case letter, a number and a minimum length. Go to the editor
Sample Output:
Input the string: W3resource
['Valid string.']

s = 'W3resource'
s1 = []
for i in s:
    if not (i.isupper() or i.islower() or i.isnumeric()) or len(s) >= 20:
        s1.append(i)
    if not s1:
        s1.append('Valid String')
print(s1)
___________________________________________________________________________________________________
Write a Python program to remove unwanted characters from a given string. Go to the editor
Sample Output:
Original String : Pyth*^on Exercis^es
After removing unwanted characters:
Python Exercises
Original String : A%^!B#*CD
After removing unwanted characters:
ABCD

s = 'Pyth*^on Exercis^es'
c = '!@#$%^&*'
s1 = ''
for i in s:
    if i not in c:
        s1 = s1 + i
print(s1)
________________________________________________________________________________________________________
Write a Python program to remove duplicate words from a given string.
Sample Output:
Original String:
Python Exercises Practice Solution Exercises
After removing duplicate words from the said string:
Python Exercises Practice Solution

s = 'Python Exercises Practice Solution Exercises'.split()
s1 = set(s)
print(" ".join(sorted(s1)))
s2 = []
for i in s:
    if i not in s2:
        s2.append(i)
print(" ".join(s2))
___________________________________________________________________________________________
 Write a Python program to convert a given heterogeneous list of scalars into a string.
Sample Output:
Original list:
['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
Convert the heterogeneous list of scalars into a string:
Red,100,-50,green,w,3,r,12.12,False

l = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]

l1 = ",".join(str(i) for i in l)
print(l1)
____________________________________________________________________________________________
Write a Python program to extract numbers from a given string. Go to the editor
Sample Output:
Original string: red 12 black 45 green
Extract numbers from the said string: [12, 45]

s = 'red 12 black 45 green'
s1 = []
for i in s.split():
    if i.isdigit():
        s1.append(i)
print(s1)
__________________________________________________________________________________________
s = 'java_Script'
if s[0].islower():
    print(s[0].upper() + s[1:])
else:
    print(s)
__________________________________________________________________________________________
Write a Python program to add two strings as they are numbers (Positive integer values).
Return a message if the numbers are string. Go to the editor
Sample Output:
42
Error in input!
Error in input!

s = '2'
s1 = 'p'

if s.isnumeric() and s1.isnumeric():
    print(s + s1)
else:
    print("Error in Input")

s = "python is very easy"
s1 = s[::-1]
print(s1)

def reverse(string):
    s1 = s[::-1]
    return s1


print(reverse("python is very easy"))
__________________________________________________________________________________________________________
Have the function LongestWord(sen) take the sen parameter being passed and
return the longest word in the string. If there are two or more words that are the same length,
return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

s = 'Hello world123 567'
s1 = max(s.split())
print(s1)

Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13

l1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
l2 = []
l3 = l1[0]
l4 = l1[1]

for i in l3:
    if i in l1[1]:
        l2.append(i)
print(l2)


l = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
l1 = set(l[0].split(","))
print(l1)
l2 = set(l[1].split(","))
print(l2)
result = l1.intersection(l2)
print(list(result))
if len(result) > 0:
    print(" ".join(result))
else:
    print("False")
'''

s = 'python'
s1 = len(s)
for i in range(s1):
    for j in range(s1):
        for k in range(s1):
            for l in range(s1):
                for m in range(s1):
                    for n in range(s1):
                        if i != j and j != k and k != l and l != m and m != n and i != n:
                            print(s[i], s[j], s[k], s[l], s[m], s[n])