from matplotlib import pyplot as plt
def listificator9000(x):
	length = len(str(x))
	digits = []
	i = -1
	string = str(x)
	while i < length - 1:
		i += 1
		digits.append(string[i])
	return digits


# fast prime number checker
def primechecker(x):
	global primes
	i = 0
	temp1 = 13
	while primes[i] < temp1:
		temp1 = x/primes[i]
		if x%primes[i] == 0:
			return False
		i += 1
	primes.append(x)
	return True

def pbl(lst, start='start'):
	print(start)
	for item in lst:
		print(item, '\n')
	print('stop')


def p(lst, title=''):
	plt.plot(lst, label=title)
	plt.title(title)
	plt.show()


def trianglefinder2000(x):
	i = 0
	total = 0
	triangles = []
	while i < x:
		i = i + 1
		total = total + i
		triangles.append(total)
	return triangles


def speedy_factorificator3000(n):
	i = 1
	factors = [1, n]
	while i < factors[-1] - 1:
		i += 1
		if n % i == 0:
			factors.append(i)
			if n / i != i:
				factors.append(n / i)
	return factors


def factorificator3000(n):
	i = 0
	factors = []
	while i < n / 2:
		i += 1
		if n % i == 0:
			factors.append(i)
			factors.append(n / i)
	factors.append(n)
	return factors


def primefactorificator5000(n, primes):
	i = -1
	pfactors = [n]
	while i < len(primes) and n != 0:
		i = i + 1
		if i == len(primes):
			i = 0
		if n % primes[i] == 0:
			pfactors.append(primes[i])
			n = n / primes[i]
		if n == 1:
			break
	return pfactors


def backwarddigificator9000(x):
	length = len(str(x))
	digits = []
	i = 0
	string = str(x)
	while i < length - 1:
		i += 1
		digits.append(string[-i])
	digits.append(string[0])
	return digits


def factorial(x):
	i = 0
	total = 1
	while i < x:
		i = i + 1
		total = total * i
	return total


def caesars_shifter9000(word, shift):
	def numberator3000(w):
		i = -1
		ascii = []
		while i < len(w) - 1:
			i += 1
			ascii.append(ord(w[i]))
		return ascii

	hello = numberator3000('hello')
	ascii = numberator3000(word)
	i = -1
	string = ''
	while i < len(ascii) - 1:
		i += 1
		ascii[i] = ascii[i] + shift
		if ascii[i] > 122:
			string = string + chr(ascii[i] - 26)
		elif ascii[i] < 97:
			string = string + chr(ascii[i] + 26)
		else:
			string = string + chr(ascii[i])

	return string


def listconcatenator9000(list):
	total = ''
	for i in range(0, len(list)):
		total = total + list[i]
	return total


class DLLnode:
	data = None
	next = None
	back = None
	length = 0

	def __init__(self,data,next=None):
		self.data = data
		self.next = next
		if next == None:
			self.length = 0
		else:
			next.back = self
			self.length = next.length


	def updateLengths(self):
		if self.next == None:
			return 1
		else:
			self.length = 1 + self.next.updateLengths()
			return self.length

	def adddata(self,data):
		if self.next == None:
			self.next = DLLnode(data)
			self.next.back = self
		else:
			self.next.adddata(data)

	def adddirect(self,data):
		self.next = DLLnode(data)
		self.next.back = self
		return self.next

	def remove(self):
		if self.back != None:
			self.back.next = self.next
		if self.next != None:
			self.back.next.back = self.back
		del self

	def first(self):
		if self.back == None:
			return self
		else:
			return self.back.first()


	def lsttoDLL(self,lst):
		node = DLLnode(lst[0]); lnth = len(lst)
		node.length = lnth
		tmp = node
		lnth -= 1
		for i in range(1,len(lst)):
			node = node.adddirect(lst[i])
			node.length = lnth; lnth -= 1
		return tmp

	def traverse(self):
		print(self.data)
		if self.next != None:
			self.next.traverse()


class BSTNode:
	data = None
	left = None
	right = None
	parent = None
	def __init__(self,data,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right

	def add(self,data):
		if type(data) != BSTNode:
			if data < self.data:
				if self.left != None:
					self.left.add(data)
				else:
					self.left = BSTNode(data)
					self.left.parent = self
			else:
				if self.right != None:
					self.right.add(data)
				else:
					self.right = BSTNode(data)
					self.right.parent = self
		else:
			if data.data < self.data:
				if self.left != None:
					self.left.add(data)
				else:
					self.left = BSTNode(data)
					self.left.parent = self
			else:
				if self.right != None:
					self.right.add(data)
				else:
					self.right = BSTNode(data)
					self.right.parent = self


	def addnode(self,node):

		if node.data < self.data:
			if self.left != None:
				self.left.addnode(node)
			else:
				self.left = node
				self.left.parent = self
		else:
			if self.right != None:
				self.right.addnode(node)
			else:
				self.right = node
				self.right.parent = self




	def root(self):
		if self.parent != None:
			return self.parent.root()
		else:
			return self


	def remove(self):
		#if self.
		pass








