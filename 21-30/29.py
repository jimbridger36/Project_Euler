
nums = []

for a in range(2,101):
	print(a)
	for b in range(2,101):
		nums.append(a**b)
print(nums)
nums1 = nums
nums = sorted(nums)
i = -1
while i < len(nums)-2:
	i += 1
	if nums[i] == nums[i+1]:
		nums.remove(nums[i+1])
		i -= 1
print(nums)
print(len(nums))