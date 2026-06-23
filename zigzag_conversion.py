# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return False
        currentrow = 0
        rows = [""] * numRows
        indicator = False
        for ch in s:
            rows[currentrow] += ch
            if currentrow == 0 or currentrow == numRows - 1:
                indicator = not indicator
            if indicator:
                currentrow += 1
            else:
                currentrow -= 1
        return "".join(rows)


# s = "AB"
# numRows = 1
s = "PAYPALISHIRING"
numRows = 3
obj = Solution()
print(obj.convert(s, numRows))
