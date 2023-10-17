ans = 76576500
number = 0
def factorfinder(n):
	i = 1
	factornumber = 2
	large_factor = n
	while i < large_factor - 1:
		i += 1
		if n % i == 0:
			factornumber += 1
			if n / i != i:
				factornumber += 1
				large_factor = n/i
	return factornumber
import time
largest = 1
largesti = 0
i1 = 0
largesti1 = 0
temp500 = []
start = time.time()
for i in range(1,20000):
	i1 += i
	temp = factorfinder(i1)
	if temp > largest:
		largest = temp
		largesti = i
		largesti1 = i1
		print(i,'..............', largest)
		if largest > 500:
			temp500 = [largest,largesti,i1]
			print('Got it ya big fat bastard')
			print(temp500)
			break
	else:
		print(i,temp)
end = time.time()
end1 = end-start

i = 1
print(largest,largesti,largesti1)
print(end1)