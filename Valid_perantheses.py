# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"


# Output: true
class Perntheses:
    def __init__(self, my_str):
        self.my_str = my_str

    def valid(self):

        stack = []
        for brakit in self.my_str:
            if brakit == "(" or brakit == "[" or brakit == "{":
                stack.append(brakit)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                # print(ch)
                if (
                    (brakit == "]" and ch == "[")
                    or (brakit == ")" and ch == "(")
                    or (brakit == "}" and ch == "{")
                ):
                    continue

                else:
                    return False

        return len(stack) == 0


s = "([)] "
obj = Perntheses(s)
print(obj.valid())


# secound method agar isko smjhna to phele khud dry run kar lena
# s = "([)] "
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {")":"(", "}":"{", "]":"["}

#         for char in s:
#             if char in mapping.values():
#                 stack.append(char)

#             elif char in mapping.keys():
#                 if not stack or mapping[char] != stack.pop():
#                     return False

#         return not stack
