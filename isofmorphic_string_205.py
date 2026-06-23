# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:


# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in map_s:
                if map_s[char_s] != char_t:
                    return False
            else:
                map_s[char_s] = char_t
            if char_t in map_t:
                if map_t[char_t] != char_s:
                    return False
            else:
                map_t[char_t] = char_s
        return True


s = "egg"
t = "add"
obj = Solution()
print(obj.isIsomorphic(s, t))
