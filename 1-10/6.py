ans = 0
sumsquares = 0
squaresum = 0
sum = 0
# getting sum of squares
for i in range(1,101):
    sumsquares += i**2

for i in range(1,101):
    sum += i
    print(i,sum)
squaresum = sum**2
ans = squaresum - sumsquares
print(sum, squaresum, ans)



