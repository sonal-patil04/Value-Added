# def Anagram(n1, n2, k):
#     freq = [0] * 10

#     while n1 != 0:
#         last_digit = n1 % 10
#         freq[last_digit] += 1
#         n1 = n1 // 10

#     while n2 != 0:
#         last_digit = n2 % 10
#         freq[last_digit] -= 1
#         n2 = n2 // 10

#     for i in freq:
#         if i != 0:
#             return False

#     return True


# n1 = 1221
# n2 = 1122
# k = 2

# res = Anagram(n1, n2, k)
# print(res)


# ---------------------------------------------------------------------
# def Anagram(n1, n2, k):
#     freq = [0] * 10

#     while n1 != 0:
#         last_digit = n1 % 10
#         freq[last_digit] += 1
#         n1 = n1 // 10

#     for i in range(10):
#         if freq[i] > k:
#             print(f"{i}---> {freq[i]}")

# n1 = 12214333
# n2 = 11223343
# k = 1

# Anagram(n1, n2, k)


# -------------------------------------------------
def countFreq(n, k):
    freq = [0] * 10

    while n != 0:
        last_digit = n % 10
        freq[last_digit] += 1
        n = n // 10

    res = []

    for i in freq:
        if freq[i]>k:
            res.append([i, freq[i]])

    return res


n=123432456674
res=countFreq(n,3)
print(res)

#-------------------------------------
# Homework
# ----------> wnat is index shifting 
# ----------> ascii table