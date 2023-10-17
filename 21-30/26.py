ans = 982
from matplotlib import pyplot as plt




def intdivide(num):
	sequence = ''
	n = 2
	newchar = str(n // num)
	nlst = [0]
	carry = n % num
	while n not in nlst:
		nlst.append(n)
		sequence += newchar
		n = 2*carry
		newchar = str(n//num)
		carry = n % num

	firstnum = nlst.index(n)
	nlst.reverse()
	secondnum = len(nlst)

	if n == 0:
		return 0
	else:
		print(sequence)
		return secondnum - firstnum



'''
b = [1,0]
lsti = [1] * 500
lstr = [0] * 500

for i in range(1,999,2):
	lsti[i//2] = i
	lstr[i//2] = intdivide(i)
	if lstr[i//2] > b[1]:
		b[0] = i
		b[1] = lstr[i//2]
'''












