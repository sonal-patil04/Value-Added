arr=[1,2,3,4,5,6,7]
k=2
r=2
temp_Arr=[]
for i in range(r):
    temp_Arr.append(arr[i])

for i in range(0, len(arr)-r, 1):
    arr[i]=arr[i+k]

j=0
for i in range(len(arr)-k, len(arr), 1):
    arr[i]=temp_Arr[j]
    j += 1

print(arr)

# output : [3, 4, 5, 6, 7, 1, 2]