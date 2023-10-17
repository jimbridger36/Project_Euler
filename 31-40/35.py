primes = [2, 3]
import time

reciprocalprimes = []


def primechecker(x):
	global primes
	i = 0
	temp1 = 13
	while primes[i] < temp1:
		temp1 = x / primes[i]
		if x % primes[i] == 0:
			return False
		i += 1
	primes.append(x)
	return True


start = time.time()
for n in range(2, 500000):
	primechecker(2 * n + 1)
end = time.time()
print(end - start)

def rotate(str,x):
	newstr1 = ''
	newstr = ['a']*len(str)
	for i in range(0,len(newstr)):
		newstr[(i+x)%len(str)] = str[i]
	for i in range(0,len(newstr)):
		newstr1 = newstr1 + newstr[i]
	return newstr1



def combos(str):
	combos = []
	for i in range(0,len(str)):
		combos.append(rotate(str,i))
	return combos

def combochecker(str):
	combos1 = combos(str)
	for i in range(0,len(combos1)):
		if (int(combos1[i]) in primes) == False:
			return False
	return True
cyclicalprimes = []
print(len(primes))
start = time.time()
for i in range(0,len(primes)):
	print(i)
	if combochecker(str(primes[i])):
		cyclicalprimes.append(primes[i])
end = time.time()
print(cyclicalprimes)
print(len(cyclicalprimes))
print(end-start)