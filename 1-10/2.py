
import math

term1=1
term2=2
term3=3

total = 2
i=0


while i<1000000 and term2<4000000:
    term5 = term2+term3
    addterm= term3
    term1=term2
    term2=term3
    term3=term5
    addterm = term5



    if addterm%2 == 0 and addterm<4000000:
        total = total + addterm
        print(str(addterm) + ', ' + str(total))

print(total)
