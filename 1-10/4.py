import math
import random
palindrome = 120700 #355*340
numbers = []
i = 0
a= 0
b= 0
c= 0

num1 = math.sqrt(palindrome)
print(num1)
num1 = round(num1)
while (a*10**5 + b*10**4 + c*10**3 + c*10**2 + b*10 + a) < 1000000:
    c=c+1
    if c>9:
        c = c-10
        b=b+1
    if b>9:
        b=b-10
        a=a+1
    palindrome = a*10**5 + b*10**4 + c*10**3 + c*10**2 + b*10 + a
    num1 = math.sqrt(palindrome)
    num1 = round(num1)
    while i != 1000000 and num1 > 400:
        num1 = round(num1)
        i = i + 1
        num1 = num1 - 1
        if float(palindrome / num1) == int(palindrome / num1) and ((palindrome/num1) < 1000) and (num1<1000):
            numbers.append(palindrome)
            numbers.append(num1)










print(numbers)






