
nums = [3,2,2,3]
val=3
j=0
for i in range(0, len(nums),1):
    if (nums[i]!=val):
        nums[j], nums[i]=nums[i],nums[j]
        j=j+1

print(nums)