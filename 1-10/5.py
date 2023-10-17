ans = 232792560

multiple = 6285399120
primes = [2,3,5,7,11,13,17,19]
numbers = []

def divisible(x):
    i=0
    while i<21:
        i=i+1
        if x%2 == 0 and x%3 == 0 and x%5 == 0 and x%7 == 0 and x%11 == 0 and x%13 == 0 and x/17 == round(x/17) and x/19 == round(x/19):
            changeable = 1
    return changeable


i = -1
while i<8:
    i = i+1
    newnumber = multiple/primes[i]
    if (divisible(newnumber)) == 1:
        print('nice one you made it')
        print(newnumber)
        numbers.append(newnumber)

print(numbers)


def inte(x):
    if x ==  round(x):
        check = 0
    return check