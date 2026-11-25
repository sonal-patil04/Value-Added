# leetcode 283
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
nums = [0,1,0,3,12]
pos=0
for i in range(len(nums)):
    if nums[i] != 0:
        temp = nums[i]

        for j in range(i, pos, -1):
            nums[j] = nums[j-1]

        nums[pos] = temp
        pos += 1

print(nums)