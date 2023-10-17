ans = 4781
def fibonacci_generator(x):
    i = 2
    fibonacci = [1,1,2,3]
    while i < x-2:
        i += 1

        number = fibonacci[i] + fibonacci[i-1]
        fibonacci.append(number)

    return fibonacci

fibonacci = fibonacci_generator(10000)
index = 0
i = -1
while i < len(fibonacci)-1:
    i += 1
    if len(str(fibonacci[i])) == 1000:
        print(i)
        index = i

print(index)