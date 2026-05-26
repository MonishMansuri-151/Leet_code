# find closest sum
lis = [-4, -1, 1, 2]
lis.sort()
target = 1
result = float()
for i in range(len(lis)):
    left = i + 1
    right = len(lis) - 1
    while left < right:
        sum = lis[i] + lis[left] + lis[right]
        if (target - sum) < (target - result):
            result = sum
        if target == sum:
            result = sum
        elif sum > target:
            right = right - 1
        elif sum < target:
            left = left + 1
print(result)
