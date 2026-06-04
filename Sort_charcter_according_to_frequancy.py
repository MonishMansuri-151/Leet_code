# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.
# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

from collections import Counter


class Solution:
    def method(self, my_str):
        count = Counter(my_str)
        # print(count)
        result = ""
        sort_char = sorted(count.items(), key=lambda x: x[1], reverse=True)
        print(sort_char)
        for ch, freq in sort_char:
            result += ch * freq
        return result


s = "tree"
obj = Solution()
print(obj.method(s))
