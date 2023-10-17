ans = [200, 375, 425]
def check(a1,b1,c1):
    if (a1 + b1 + c1 == 1000) and (a1**2 + b1**2 == c1**2):
        print(a1,b1,c1)
        global ans
        ans.append([a1, b1, c1])
        return True
ans = []

for i in range(200,600):
    c = i
    for i in range(1,500):
        a = i
        b = 1000 - c - a
        check(a,b,c)




