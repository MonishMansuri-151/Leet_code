class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.num = nums
        left = 0
        for right in range(len(self.num)):
            if self.num[left] != self.num[right]:
                left += 1
                self.num[left], self.num[right] = self.num[right], self.num[left]
        return left + 1


arr = [1, 1, 2]
obj = Solution()
x = obj.removeDuplicates(arr)
print(x)
print(arr)
