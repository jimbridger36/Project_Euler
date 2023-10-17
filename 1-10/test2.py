def bubblesort(list):
    smaller = []
    larger = []
    final = []
    beginning = []
    hold = []
    length = len(list)
    i = round(length/2)
    i1 = i
    while i < length-1:
        i += 1
        if list[i] <= i1:
            smaller.append(list[i])
        else:
            larger.append(list[i])
    final = smaller + larger
    return larger
print(bubblesort([1,7,2,0]))
