# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:


# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1
# two pointer approch
class Solution(object):
    def Count_Fruits(self, nums):
        maxi = 0
        right = 0
        left = 0
        my_dict = {}
        while right < len(nums):
            my_dict[nums[right]] = my_dict.get(nums[right], 0) + 1
            print(my_dict)
            if len(my_dict) > 2:
                my_dict[nums[left]] -= 1
                if my_dict[nums[left]] == 0:
                    del my_dict[nums[left]]
                left += 1
            if len(my_dict) <= 2:
                maxi = max(maxi, right - left + 1)
                print(maxi)
            right += 1
        return maxi


arr = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
obj = Solution()
print(obj.Count_Fruits(arr))


# brut force approch
# class Solution(object):
#     def Count_Fruits(self, nums):
#         maxi = 0
#         for i in range(len(nums)):
#             my_set = set()
#             j = i
#             while j < len(nums):
#                 my_set.add(nums[j])
#                 print(my_set)
#                 if len(my_set) > 2:
#                     break
#                 maxi = max(maxi, j - i + 1)
#                 j = j + 1
#             print("_______________________")
#         return maxi


# arr = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
# obj = Solution()
# print(obj.Count_Fruits(arr))
