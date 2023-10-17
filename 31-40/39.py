answers = []
def check(a1,b1,c1,p):
	if (a1 + b1 + c1 == p) and (a1**2 + b1**2 == c1**2):
		return True
	return False

def find(p):
	global answers
	ans = []
	for a in range(1,int(p/1.5)):
		for c in range(a,int(p/1.25)):
			b = p - a - c
			if check(a,b,c,p) and a < b:
				ans.append([a,b,c])
	answers.append(ans)

for i in range(0,1001):
	print(i)
	find(i)
lengths = []
for i in range(0,1001):
	lengths.append([len(answers[i]),i])
print(sorted(lengths))
