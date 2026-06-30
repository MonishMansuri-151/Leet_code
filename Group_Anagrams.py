# 49. Group Anagrams
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
class Solution:
    def Anagrams(self, strs):
        my_dict = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(strs[i])
        return list(my_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
print(obj.Anagrams(strs))
