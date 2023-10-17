number1 = 2**1000
number = str(number1)

def  digitificator9000(x):
    length = len(str(x))
    digits = []
    i = -1
    string = str(x)
    while i<length-1:
        i += 1
        digits.append(int(string[i]))
    return digits


digits = digitificator9000(number)
print(sum(digits))