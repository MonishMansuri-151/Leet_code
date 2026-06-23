# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:


# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import Counter

        left = 0
        freqs1 = Counter(s1)
        window = Counter(s2[: len(s1)])
        if freqs1 == window:
            return True
        for right in range(len(s1), len(s2)):
            window[s2[right]] += 1
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1
            if window == freqs1:
                return True
        return False


s1 = "ab"
s2 = "eidbaooo"
obj = Solution()
print(obj.checkInclusion(s1, s2))
