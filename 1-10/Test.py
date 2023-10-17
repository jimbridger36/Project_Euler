
list = [7,2,6,0,10,12,4,11,19]
smaller = []
larger = []
final = []
beginning = []
hold = []
length = len(list)
i1 = int(length/2)
i = -1
print(i1)
def splitin2(list):
    i = -1
    length = len(list)
    i1 = int(len(list)/2)
    while i < length-1:
        i += 1
        if list[i] < list[i1]:
            smaller.append(list[i])
        else:
            larger.append(list[i])
    howdy = [0,0]
    howdy[0] = smaller
    howdy[1] = larger
print(smaller)
print(larger)
print(splitin2([7,2,8,4,1,123]))

