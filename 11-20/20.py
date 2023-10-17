def  backwarddigificator9000(x):
    length = len(str(x))
    digits = []
    i = 0
    string = str(x)
    while i<length-1:
        i += 1
        digits.append(int(string[-i]))
    digits.append(int(string[0]))
    return digits


def factorial(x):
    i = 0
    total = 1
    while i < x:
        i = i+1
        total = total*i

    return total

limit = 100

facc = factorial(limit)
print(facc)
digits = backwarddigificator9000(facc)
print(digits)
print(sum(digits))