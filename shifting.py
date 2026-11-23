# right shifting
# arr=[5,10,15,20,25,30,35]
# pos=3
# for i in range(len(arr)-1,pos-1,-1):
#     arr[i]=arr[i-pos]
# for i in range(pos):
#     arr[i]=0
# print(arr)
# o/p=[0, 0, 0, 5, 10, 15, 20]


# ---------------------------------------------------------------------------
# left shifting
# arr=[5,10,15,20,25,30]
# pos=1
# for i in range(0,len(arr)-pos):
#     arr[i]=arr[i+pos]                #[10, 15, 20, 25, 30, 30]
# for i in range(-1,pos-1):
# # for i in range(len(arr)-pos,len(arr),1):
#     arr[i]=0                        #[10, 15, 20, 25, 30, 0]
# print(arr)


# o/p=[10,15,20,25,30,0]



# ---------------------------------------------------------------------------
# arr = [5,10,15,20,25,30,35]
# pos = 3
# for i in range(len(arr)-pos, len(arr)):
#     arr[i] = 0
# print(arr)


# o/p=[5,10,15,20,0,0,0]

# ------------------------------------------------------------------------------------------
# adding element to specific position
# arr=[5,10,20,25]
# pos=2
# insert=15
# for i in range(len(arr)-1,pos-1,-1):
#     arr[i]=arr[i-1]
# arr[pos]=insert
# print(arr)


# -----------------------------------------------------------------------------------
# deleting 15 and left shifting
# arr = [5,10,15,20,25,30]
# pos = 2
# for i in range(pos, len(arr)-1,1):
#     arr[i] = arr[i+1]

# arr[-1]=0
# print(arr)


# -----------------------------------------------------------------------------------
# deleting 15 and right shifting
# arr = [5,10,15,20,25,30]
# pos = 2
# for i in range(pos, 0, -1):
#     arr[i] = arr[i-1]
# arr[0]=0
# print(arr)

    
# -----------------------------------------------------------------------------------
# deleting x occurence and shift non-occurence elements to left
# o/p = [20,30,40,0,0,0]
# arr=[10,20,10,30,10,40]
# x=10
# j=0
# for i in range(len(arr)):
#     if arr[i]!=x:
#         arr[j]=arr[i]
#         j+=1

# for i in range(j,len(arr)):
#     arr[j]=0
#     j+=1

# print(arr)




# ------------------------------------------------------------------------------
# shifting all 0 to right(end of array) and non-zero to left 
# arr = [0,1,0,3,12]
# j=0
# for i in range(0,len(arr),1):
#     if arr[i]!=0:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         j+=1

# print(arr)