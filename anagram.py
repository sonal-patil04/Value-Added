# n1=1221
# n2=1212

# freq1=[0]*10
# while(n1!=0):
#     last_digit=n1%10
#     freq1[last_digit]+=1
#     n1=n1//10

# freq2=[0]*10
# while(n2!=0):
#     last_digit=n2%10
#     freq2[last_digit]+=1
#     n2=n2//10



# if freq1==freq2:
#     print("Anagram")
# else:
#     print("Not anagram")


# -------------------------------------------------

# using def function

# def Anagram(n1,n2):

#     freq=[0]*10

#     while(n1!=0):
#         last_digit=n1%10
#         freq[last_digit]+=1
#         n1=n1//10


#     while(n2!=0):
#         last_digit=n2%10
#         freq[last_digit]-=1
#         n2=n2//10


#     for i in freq:
#         if (i!=0):
#             return false
#     return True

# n1=1221
# n2=1122

# res=Anagram(n1,n2)

# print(f"{n1} and {n2} are anagram")
# print(f"{res}")


# -------------------------------------------------------------------

def Anagram(n1,n2,k):

    freq=[0]*10

    while(n1!=0):
        last_digit=n1%10
        freq[last_digit]+=1
        n1=n1//10


    while(n2!=0):
        last_digit=n2%10
        freq[last_digit]-=1
        n2=n2//10


    for i in freq:
        if (i!=0):
            return False
    return True


n1=1221
n2=1122
k=2


res=Anagram(n1,n2,k)

