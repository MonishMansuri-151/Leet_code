class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set(nums)
        longest = 0
        for num in my_set:
            if num - 1 not in my_set:
                count = 1
                x = num
                while x + 1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest


arr = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
obj = Solution()
print(obj.longestConsecutive(arr))
# class Solution:
#     def longestConsecutive(self, nums):
#         num_set = set(nums)
#         longest = 0

#         for num in num_set:

#             # sirf sequence ke start se count karo
#             if num - 1 not in num_set:

#                 current = num
#                 length = 1

#                 while current + 1 in num_set:
#                     current += 1
#                     length += 1

#                 longest = max(longest, length)

#         return longest


# arr = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
# obj = Solution()
# print(obj.longestConsecutive(arr))
