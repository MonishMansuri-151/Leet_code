# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings
class CommonPrefix:
    def __init__(self, my_arr):
        # Array ko sort karenge
        my_arr.sort()

        # First aur last string store karenge
        self.start = my_arr[0]
        self.end = my_arr[-1]

    def prefix(self):
        i = 0
        temp = ""

        # Common characters check karenge
        while i < len(self.start) and i < len(self.end):
            if self.start[i] == self.end[i]:
                temp += self.start[i]
            else:
                break
            i += 1

        return temp


# Input
arr = ["flower", "flow", "flight"]

# Object create
obj = CommonPrefix(arr)

# Function call
x = obj.prefix()

print(x)
