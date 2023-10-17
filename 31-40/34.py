ans = [145,40585,]
def factorial(x):
	i = 0
	total = 1
	while i < x:
		i = i + 1
		total = total * i
	return total
print(factorial(10))


nums = []
faccs = []



def faccheck(x):
	total = 0
	for i in range(0, len(x)):
		total = total + factorial(int(x[i]))
	if total == int(x):
		return True
	else:
		return False

for i in range(1000000, 10000000):
	if faccheck(str(i)) == True:
		faccs.append(str(i))
print(faccs)