ans=233168


total = 0
i=0
num=1

while i != 999:
    if num%3==0 and num%5!=0:
        total=total+num
        print(str(num) + ', ' + str(total))

    elif num%3!=0 and num%5==0:
        total=total+num
        print(str(num) + ', ' + str(total))

    elif num%3==0 and num%5==0:

        total=total+num
        print(str(num) + ', ' + str(total))

    num=num+1
    i=i+1
