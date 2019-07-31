#!/usr/local/bin/python3


nums = [x for x in range(1,101)]
del nums[65]

print(nums)

if (nums[0] != 1):
	print("the missing number is: 1")
	exit()
for index in range(98):
	if (nums[index+1] != (nums[index] + 1)):
		print("the missing number is: ",nums[index] + 1)

for i in range(1,101):
	if (not (i in nums)):
		print("the missing number is: ",i)


nums.append(37)
print(nums)

for item in nums:
	if (nums.count(item) > 1):
		print("the duplicate entry is: ",item)

print("array min is: ",min(nums))
print("array max is: ",max(nums))
