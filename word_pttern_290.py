# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        map_char = {}
        map_word = {}
        word_list = s.split()
        if len(pattern) != len(word_list):
            return False
        for char, word in zip(pattern, word_list):
            if char not in map_char:
                if word in map_word:
                    return False
                else:
                    map_char[char] = word
                    map_word[word] = char
            else:
                if map_char[char] != word:
                    return False
        return True


pattern = "abba"
s = "dog cat cat dog"
obj = Solution()
print(obj.wordPattern(pattern, s))
