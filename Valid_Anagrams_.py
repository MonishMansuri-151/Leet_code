# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
class Solution:
    def Valid_Anagram(self, s, t):
        countS = {}
        countT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        print(countS)
        print(countT)
        return countT == countS


# s = "a"
# t = "ab"
s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.Valid_Anagram(s, t))
