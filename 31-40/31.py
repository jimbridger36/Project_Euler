coins = []
p2 = ['2p']
p5 = ['2p 2p 1p']
p10 = ['5p 5p']
p20 = ['10p 10p']
p50 = ['20p 20p 10p']
p100 = ['50p 50p']
p200 = ['100p 100p']

ip2 = ['2p']
ip5 = ['2p 2p 1p']
ip10 = ['5p 5p']
ip20 = ['10p 10p']
ip50 = ['20p 20p 10p']
ip100 = ['50p 50p']
ip200 = ['100p 100p']
def sorter(string):
	list1 = string.split()
	coinnumbers = [list1.count('1p'), list1.count('2p'),list1.count('5p'),list1.count('10p'),list1.count('20p'),list1.count('50p'),list1.count('100p'),list1.count('200p')]
	return coinnumbers

def choiceificator():
	



