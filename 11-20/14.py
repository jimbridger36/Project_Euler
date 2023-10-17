ans = [837799, 525]
ac = {}
a = {}
import time
from sys import getsizeof as gs
#up to 100mil gives [63728127, 950]
'''def collatz(num):
	if num in answercache:
		return answercache[num]
	if num % 2 == 0:
		result = collatz(num//2)+1
	else:
		result = collatz(3*num+1)+1

	answercache[num] = result
	return result


def umcollatz(num):
	print(num)
	if num == 1:
		return 0
	elif num % 2 == 0:
		result = umcollatz(num//2)+1
	else:
		result = umcollatz(3*num+1)+1
	return result
'''
start = time.time()
max = [1,1]
for i in range(0,1000000):
	ac[i] = None
	a[str(i)] = None
print(time.time()-start)
