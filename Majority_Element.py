# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋
#  times. You may assume that the majority element always
# exists in the array.
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
class Solution:

    def frequncry(self, nums):
        my_dict = {}
        lenght = len(nums) // 2
        print(lenght)
        for n in nums:
            my_dict[n] = my_dict.get(n, 0) + 1
        print(my_dict)
        for key, value in my_dict.items():
            if value > lenght:
                return key


arr = [2, 2, 1, 1, 1, 2, 2]
arr = sorted(arr)
obj = Solution()
print(obj.frequncry(arr))
