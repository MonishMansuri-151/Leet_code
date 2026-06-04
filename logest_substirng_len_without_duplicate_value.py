# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:


# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# brute force approch


def sub_long(my_str):

    maxi = 0
    i = 0
    while i < (len(my_str)):
        j = i
        my_set = set()
        while j < len(my_str):
            if my_str[j] in my_set:
                break

            else:
                print(my_str[j], end=" ")
                my_set.add(my_str[j])
                maxi = max(maxi, j - i + 1)
            j = j + 1
        print("")
        i = i + 1
    return maxi


a = "CADBZABCD"
x = sub_long(a)
print(x)


# # two pointer approch
# right = 0
# left = 0
# my_dict = {}
# my_str = "CADBZABCD"
# maxi = 0

# while right < len(my_str):
#     if my_str[right] in my_dict:
#         left = max(left, my_dict[my_str[right]] + 1)

#     maxi = max(maxi, right - left + 1)
#     my_dict[my_str[right]] = right
#     right = right + 1
#     # print(my_dict[my_str[right]])
# print(maxi)
# agar isko smajha to phele dry run kara kyunki iska dry run remaninig he
