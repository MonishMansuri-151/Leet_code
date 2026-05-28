# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class Slution:
    val = 2

    def __init__(self, num, k):
        self.num = num
        self.k = k

    def method(self):
        for i in range(len(self.num)):
            if self.val == self.num[i]:
                continue
            else:
                self.num[self.k] = self.num[i]
                self.k += 1
        return self.k


arr = [0, 1, 2, 2, 3, 0, 4, 2]
obj = Slution(arr, k=0)
print(obj.method())
print(arr)
