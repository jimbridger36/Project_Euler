def abundant(x):
	factors = []
	i = 0
	while i < x-1:
		i += 1
		if x % i == 0:
			factors.append[i]
	true = 0
	if sum(factors)>x:
		true = 1
	return true
import time
print('1')
def abundants(x):
	abundantnums = []
	def abundant(x):
		howdies = []
		i = 0
		while i < (x/2):
			i += 1
			if x % i == 0:
				howdies.append(i)
		true = 0
		if sum(howdies) > x:
			true = 1
		return true
	i = 0
	while i < x-1:
		i += 1
		if abundant(i) == 1:
			abundantnums.append(i)
	return abundantnums
start = time.time()
Anums = abundants(28123)
end = time.time()
print(end-start, 'to make the Anums')
print('2')
print(Anums)

def abundant_checker(Amicaables, x):
	hello = False
	for i in range(0, len(Amicaables) - 1):
		if ((x-Amicaables[i]) in Amicaables) == True:
			hello = True
			break
	return hello
print('3')
helper = []
i = -1
start = time.time()
end1 = 0
while i < 28123:
	i += 1
	start1 = time.time()
	if abundant_checker(Anums, i) == True:
		helper.append(i)
		print(start1-end1, helper[-1])
	end1 = time.time()
end = time.time()
print(end-start)
print(helper)
print(sum(helper))



print('4')




