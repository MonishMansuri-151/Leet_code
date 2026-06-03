# Given an integer array nums and an integer k, return the k most frequent elements
# . You may return the answer in any order.
# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1, 2]


from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        print(count)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans


arr = [1, 1, 1, 2, 2, 3]
k = 2
obj = Solution()
print(obj.topKFrequent(arr, k))
