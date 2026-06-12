class Solution:
    def removeDuplicates(self, nums):
        nums_counter = {}
        k = 0

        for n in nums:
            nums_counter[n] = nums_counter.get(n, 0) + 1
            if nums_counter[n] <= 2:
                nums[k] = n
                k += 1
        return k


arr = [1, 1, 1, 2, 2, 3]
obj = Solution()
print(obj.removeDuplicates(arr))
