# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
class Slution:
    def __init__(self, num1, num2, m, n):
        self.num1 = num1
        self.num2 = num2
        self.m = m
        self.n = n

    def merge_sort(self):
        i = self.m - 1
        j = self.n - 1
        k = self.m + self.n - 1
        while i >= 0 and j >= 0:
            if self.num1[i] > self.num2[j]:
                self.num1[k] = self.num1[i]
                i = i - 1
            else:
                self.num1[k] = self.num2[j]

                j = j - 1
            k = k - 1
        return self.num1


a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]
m = 3
n = 3
obj = Slution(a, b, m, n)
print(obj.merge_sort())
