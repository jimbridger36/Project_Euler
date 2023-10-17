ans = [4150, 4151, 54748, 92727, 93084,194979]
print(sum(ans))
nums = []
for i in range(500000,1000000):
	nums.append(str(i))
fifthpowers = []
def fifthpowerchecker(x):
	total = 0
	for i in range(0,len(x)):
		total = total + (int(x[i]))**5
	if total == int(x):
		return True
	return False

for i in range(0,len(nums)):
	if fifthpowerchecker(nums[i]):
		fifthpowers.append(nums[i])

print(fifthpowers)