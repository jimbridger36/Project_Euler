#triangle creator
triangles = []
pentagonals = []
hexagonals = []
for n in range(0,300000):
	triangles.append(int(n*(n+1)/2))
for n in range(0,160000):
	pentagonals.append(int(n*(3*n-1)/2))
for n in range(0,150000):
	hexagonals.append(int(n*(2*n-1)))
y = triangles[-1]
print(triangles[-1]/y,pentagonals[-1]/y,hexagonals[-1]/y)

trues = []
def check(x):
	if ((x in triangles) and (x in hexagonals)) and (x in pentagonals):
		global trues
		trues.append(x)
		return True
	return False
for i in range(0,len(hexagonals)):
	print(i)
	if check(hexagonals[i]):
		print(trues)




