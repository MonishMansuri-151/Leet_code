class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set()
        n = len(nums)
        for i in range(0, n):
            my_set.add(nums[i])
            longest = 0
            for num in my_set:
                if num - 1 not in my_set:
                    count = 1
                    x = num
                    while x + 1 in my_set:
                        count += 1
                        x += 1
                    longest = max(longest, count)
        return longest


arr = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
obj = Solution()
print(obj.longestConsecutive(arr))
