#prime number checker
#started at 5.36.00
#stopped at 6.15.00
#started at 6.18.00 (printing primes)
#finished at
#1150000 at 6.54
#1250000 at 7.00
#1600000 at 7.23
#1700000 at 7.30
#1800000 at 7.37
#finished at 7.53
#total = 1 hour 30
primes = [2]
num = 1000
n = 1
while n < num:
    n = n+2
    primeornot = 1
    i=-1
    while i < len(primes) - 1:
        primeornot = 1
        i = i + 1
        if n % primes[i] == 0:
            primeornot = 0
            break

    if primeornot == 1:
        primes.append(n)
        print(n)



print(sum(primes))
print(primes[10000])

def primecheck(number):
    primeornot = 1
    iteration10 = number
    for iteration10 in range(562, number):
        if number/iteration10 == round(number/iteration10):
            primeornot = 0
            break
    else:
        primeornot = 1

    return primeornot


