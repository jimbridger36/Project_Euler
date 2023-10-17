digits = ['4','3','2','1','0']
lenlist = len(digits)
def factorial(x):
	i = 0
	total = 1
	while i < x:
		i = i+1
	total = total*i
	return total

def listconcatenator9000(list):
	total = ''
	for i in range(0,len(list)):
		total = total + list[i]
	return total

def exchanger(list,x):
	for i in range(x,lenlist-1):
		if list[i] == list[x]:
			list[i] = str((int(list[i]) - 1) % lenlist)
			return listconcatenator9000(list)
	for i in range(x,len(list)):
		if list[i] == list[x]:
			list[i] = str((int(list[i]) - 1) % lenlist)



list1 = ['0','1','2','3','4']
def increasedigit(list,x):
	list[x] = str((int(list[x])+1)%lenlist)
	return list

def  backwarddigificator9000(x):
	length = len(str(x))
	digits = []
	i = 0
	string = str(x)
	while i<length-1:
		i += 1
		digits.append(string[-i])
	digits.append(string[0])
	return digits
listnums = []
for i in range(0,24):
	digits = increasedigit(digits,0)
	listnums.append(listconcatenator9000(exchanger(digits,0)))
	print(listnums)

print(listnums)

