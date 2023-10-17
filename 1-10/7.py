totals = []

def change(x):
    if x % 2 == 0:
        y = x / 2
    if x % 2 != 0:
        y = 3 * x + 1
    return y


def total(num):
    i = 1
    while num != 1:
        num = int(change(num))
        i = i + 1

    return i

while num<1000000000 and num>1:
    num = num-1
    n = num
    totals.append(total(n))
    if total(n) > 500:
        print(str(n) + ', ' + str(total(n)))

print('found')

totals1 = []
i = -3
while i < int(len(totals))-3:
    i=i+3
    if totals[i]>totals[i+1] and totals[i]>totals[i+2]:
        totals1.append(totals[i])
    if totals[i+1]> totals[i] and totals[i+1]>totals[i+2]:
        totals1.append(totals[i+1])
    if totals[i+2]> totals[i] and totals[i+2]>totals[i+1]:
        totals1.append(totals[i+2])

totals2 = []
i = -3
while i < int(len(totals1))-3:
    i=i+3
    if totals1[i]>totals1[i+1] and totals1[i]>totals1[i+2]:
        totals2.append(totals1[i])
    if totals1[i+1]> totals1[i] and totals1[i+1]>totals1[i+2]:
        totals2.append(totals1[i+1])
    if totals1[i+2]> totals1[i] and totals1[i+2]>totals1[i+1]:
        totals2.append(totals1[i+2])

totals3 = []
i = -3
while i < int(len(totals2))-3:
    i=i+3
    if totals2[i]>totals2[i+1] and totals2[i]>totals2[i+2]:
        totals3.append(totals2[i])
    if totals2[i+1]> totals2[i] and totals2[i+1]>totals2[i+2]:
        totals3.append(totals2[i+1])
    if totals2[i+2]> totals2[i] and totals2[i+2]>totals2[i+1]:
        totals3.append(totals2[i+2])
totals3.append(10)
totals3.append(20)

totals4 = []
i = -3
while i < int(len(totals3))-3:
    i = i+3
    if totals3[i]>totals3[i+1] and totals3[i]>totals3[i+2]:
        totals4.append(totals3[i])
    if totals3[i+1]> totals3[i] and totals3[i+1]>totals3[i+2]:
        totals4.append(totals3[i+1])
    if totals3[i+2]> totals3[i] and totals3[i+2]>totals1[i+1]:
        totals4.append(totals3[i+2])



print(len(totals))
print(totals1)
print('ur mum gay')
print(totals2)
print('ur mum mega gay')
print(totals3)
print('ur mum mega extra gay')
print(totals4)

print('howdy ')



