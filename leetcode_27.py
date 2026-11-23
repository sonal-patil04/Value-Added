
# nums = [3,2,2,3,2]
nums= [0,1,2,2,3,0,4,2]
val=2
j=0
count=0
for i in range(0, len(nums),1):
    if (nums[i]!=val):
        nums[j], nums[i]=nums[i],nums[j]
        j=j+1
        count=count+1

print(nums)
print(count)