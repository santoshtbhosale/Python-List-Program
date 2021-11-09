'''
s = 'google.com'
a = list(s)
a.extend(a)
a.remove('.')
for i, item in enumerate(a):
    print(i,item,end=':')
d = dict()
print()

n = int(input("Enter the Number:"))
a = 0
b = 1
for i in range(2,n):
    c = a + b
    a = b
    b = c
    print(b)

n = input("Enter the Number:")

count = 0
for j in n:
    count = count + int(j)
print(count)

n = int(input("Enter the Number:"))
count = 0
while n > 0:
    count = count + 1
    n = n // 10
print(count)

count = 0


def counting(number):
    global count
    if number > 0:
        count = count + 1
        counting(number // 10)
        return count


number = int(input("Please enter the number only"))
count1 = counting(number)
print(count1)




n = int(input("Enter the Number:"))
s = str(n)
if s == s[::-1]:
    print("The Given Number is Palindrome")
else:
    print("The Given number is not Palindrome")

n = int(input("Enter the Number:"))
s = str(n)
s1 = ''
for i in s[::-1]:
    s1 = s1 + i
if s == s1:
    print("The nuumber is palindrome")
else:
    print("The number is not palindrome")



def palindrome(number):
    s = str(number)
    s1 = ''
    for i in s[::-1]:
        s1 = s1 + i
    if s == s1:
        print("The number is palindrome")
    else:
        print("The number is not palindrome")


number = int(input("Enter the Number:"))
palindrome(number)

n = 5

for i in range(1, n+1):
    for j in range(1,n+2-i):
        print('*', end=" ")
    print()
'''
for i in range(400, 500):
    if i % 10 == 7:
        print(i,end=" ")