# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
# Example 1:


# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
class Solution:
    def maximum_subarray_Average(self, nums, k):
        window = sum(nums[:k])
        left = 0
        # 1,12,-5,-6,ye k ke baraber he inka sum 2 he window ka
        ans = window / k
        for right in range(k, len(nums)):
            window += nums[right] - nums[left]
            left += 1
            ans = max(ans, window / k)
        return ans


arr = [1, 12, -5, -6, 50, 3]
k = 4
obj = Solution()
print(obj.maximum_subarray_Average(arr, k))
