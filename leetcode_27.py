
nums = [3,2,2,3]
val=3
j=0
for i in range(0, len(nums),1):
    if (nums[i]!=val):
        nums[i], nums[j]=nums[j],nums[i]
        j=j+1

print(nums)