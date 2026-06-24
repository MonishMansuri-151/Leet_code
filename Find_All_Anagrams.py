# 438. Find All Anagrams in a String
# Medium
# Topics
# premium lock icon
# Companies
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# Example 1:


# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter

        n = len(s)
        m = len(p)
        if n < m:
            return []
        p_count = Counter(p)
        print(p_count)
        window_right = Counter(s[:m])
        print(window_right)
        ans = []
        if p_count == window_right:
            ans.append(0)
        for i in range(m, n):
            window_right[s[i]] += 1
            # print(window_right)
            left_char = s[i - m]
            # print(left_char)
            window_right[left_char] -= 1

            # print(window_right)
            if window_right[left_char] == 0:
                del window_right[left_char]
            # print(window_right)
            # left_char += 1
            if p_count == window_right:
                ans.append(i - m + 1)
        return ans


# s = "cbaebabacd"
# p = "abc"
s = "hello"
p = "ll"
obj = Solution()
print(obj.findAnagrams(s, p))
