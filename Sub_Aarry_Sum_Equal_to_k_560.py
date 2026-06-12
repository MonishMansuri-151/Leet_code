# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:


# Input: nums = [1,2,3], k = 3
# Output: 2
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prifix_sum = 0
        my_dict = {0: 1}
        result = 0

        for num in nums:
            prifix_sum += num
            if prifix_sum - k in my_dict:
                result = result + my_dict[prifix_sum - k]
                # print(result)
            if prifix_sum not in my_dict:
                my_dict[prifix_sum] = 1
            else:
                my_dict[prifix_sum] += 1
        return result


nums = [1, 1, 1]
k = 2
obj = Solution()
print(obj.subarraySum(nums, k))
