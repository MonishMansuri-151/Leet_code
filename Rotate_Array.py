# Given an integer array nums, rotate the array to the right by k steps,
#  where k is non-negative.
# Example 1:


# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 3 appproch to solve this  qution
# 1. brutforce approch loop 0 to k and pop ele and insert satrt
# 2. slice kth part and + remaninig part
# tow pointer apporch to left to right
# using two pointer approch solve this queiton
class Solution:
    def method(self, nums, left, right):
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1


arr = [1, 2, 3, 4, 5]
k = 2
obj = Solution()
obj.method(arr, len(arr) - k, len(arr) - 1)
obj.method(arr, 0, len(arr) - k - 1)
obj.method(arr, 0, len(arr) - 1)
print(arr)
