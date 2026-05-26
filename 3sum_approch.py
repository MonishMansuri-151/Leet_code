# 18. Find Triplets That Sum to Zero
# Given a list of numbers, find all unique triplets (a, b, c) such that a + b + c = 0.
# a. numbers = [-1, 0, 1, 2, -1, -4]
# b. Expected Output: [(-1, -1, 2), (-1, 0, 1)]
lis = [-1, 0, 1, 2, -1, -4]
lis.sort()
# print(lis)
size = len(lis)
ans = []
for i in range(size):
    if i > 0 and lis[i] == lis[i - 1]:
        continue
    j = i + 1
    sum = 0
    k = len(lis) - 1
    while j < k:
        sum = lis[i] + lis[j] + lis[k]
        if sum < 0:
            j = j + 1
        elif sum > 0:
            k = k - 1
        else:
            ans.append([lis[i], lis[j], lis[k]])
            j = j + 1
            k = k - 1
            while j < k and lis[j] == lis[j - 1]:
                j = j + 1

print(ans)
