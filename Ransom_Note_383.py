# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:


# Input: ransomNote = "aa", magazine = "ab"
# Output: false
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        my_dict1 = {}
        my_dict2 = {}
        for ch in range(len(ransomNote)):
            my_dict1[ransomNote[ch]] = my_dict1.get(ransomNote[ch], 0) + 1
        for ch in range(len(magazine)):
            my_dict2[magazine[ch]] = my_dict2.get(magazine[ch], 0) + 1
        for i in ransomNote:
            if my_dict2.get(i, 0) < my_dict1[i]:
                return False
        return True


ransomNote = "aa"
magazine = "ab"
obj = Solution()
print(obj.canConstruct(ransomNote, magazine))
