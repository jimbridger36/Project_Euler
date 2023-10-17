def speedy_factorificator3000(n):
    i = 1
    factors = [1, n]
    while i < factors[-1]-1:
        i += 1
        if n % i == 0:
            factors.append(i)
            if n/i != i:
                factors.append(n/i)
    factors.remove(factors[1])
    return factors
def factorificator3000(n):
    i = 0
    factors = []
    while i < n-1:
        i += 1
        if n % i == 0:
            factors.append(i)
    return factors
print(sum(factorificator3000(220)))


def amicable(x):
    y = sum(factorificator3000(x))
    if (sum(factorificator3000(y)) == x) and x != y:
        global amicables
        amicables.append(x)
amicables = []
for i in range(1,10001):
    print(i)
    amicable(i)
print(sum(amicables))




