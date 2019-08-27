#!/usr/bin/pypy3

nums = [0] * 24

maxnum = 7
pointer = len(nums)-1

while (True):
    print(nums)
    # increment number at pointer
    nums[pointer] += 1

    # now check if it rolled over
    if (nums[pointer] > maxnum):
        if (pointer == 0): exit(0)

        while(nums[pointer] > maxnum):
            pointer -= 1
            nums[pointer] += 1

        # set to zero and everything to the right
        for i in range(pointer+1,len(nums)): nums[i] = 0

        pointer = len(nums) - 1
