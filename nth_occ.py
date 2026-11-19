# n=12357213908
# freq=[0]*10

# while(n!=0):
#     last_digit=n%10
#     freq[last_digit]+=1
    
#     n=n//10

# print(freq)





# with def function-------------->
def countFreq(n):
    # n=12357213908
    freq=[0]*10

    while(n!=0):
        last_digit=n%10
        freq[last_digit]+=1
    
        n=n//10

    return freq


# res=countFreq(n)
# for i in range(len(res)):
#     print(f'{i}--> {res[i]}')