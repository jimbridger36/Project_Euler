# ans = 21124
digits = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve'
    ,'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
thou = 'onethousand'

def type(num1):
    string = ''
    numstr1 = str(num1)
    if len(numstr1) > 2 :
        if numstr1[-1] == '0' and numstr1[-2] == '0':
            string = string + digits[int(numstr1[-3])] + 'hundred'
        else:
            string = string + digits[int(numstr1[-3])] + 'hundredand'

    if len(numstr1) > 1:
        if numstr1[-2] == '1':
            string = string + digits[int(numstr1[-2] + numstr1[-1])]
            return string
        else:
            string = string + tens[int(numstr1[-2])] + digits[int(numstr1[-1])]
            return string
    else:
        string = string + digits[num1]
    return string

totalchars = 0
totalstring = ''
for i in range(1,1000):
    totalstring +=  type(i)
    totalchars += len(type(i))
totalstring += thou
totalchars += len(thou)
print(len(totalstring), totalstring)
print(totalchars)








