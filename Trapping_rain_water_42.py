# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped
class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        right = len(nums) - 1
        left = 0
        max_left = 0
        max_right = 0
        ans = 0
        while left < right:
            max_left = max(max_left, nums[left])
            max_right = max(max_right, nums[right])
            if max_left < max_right:
                ans += max_left - nums[left]
                left += 1
            else:
                ans += max_right - nums[right]
                right -= 1
        return ans


height = [4, 2, 0, 3, 2, 5]
obj = Solution()
print(obj.trap(height))
