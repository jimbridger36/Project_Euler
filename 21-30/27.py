ans = -59231
import cfunction as c
import Functions as functions

def primefactorificator5000(n,primes):
    i = -1
    pfactors = [n]
    while i<len(primes) and n !=0:
        i = i+1
        if i == len(primes):
            i=0
        if n%primes[i] == 0:
            pfactors.append(primes[i])
            n = n/primes[i]
        if n == 1:
            break
    return pfactors

def primecheck(number):
    for i in range(0,len(primes)):
        if number%primes[i] == 0:
            return False
    return True

def pc(num):
    return num in primesd




primes = functions.primese5
primesd = functions.primesd

print(len(primes))
print(len(primesd))


bcn = [-79,1601,0]
def numchecker(b,c):
    x = 0
    while (x*x + b*x + c) in primesd:
        x += 1
    return x
num = [80, -79, 1601]
d = {}
for i in range(10000):
    d[i] = i

bcn = [1,3,0]

for c in range(167):

    for b in range(-999,999,2):
        if numchecker(b,primes[c]) > bcn[2]:
            bcn = [b,primes[c],numchecker(b,primes[c])]










