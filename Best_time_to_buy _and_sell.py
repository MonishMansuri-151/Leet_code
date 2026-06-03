# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:


# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
class Solution:
    def max_profit(self, prices):
        buy_price = 0
        current = 1
        profit = 0

        while current < len(prices):

            if prices[buy_price] < prices[current]:
                profit = max(profit, prices[current] - prices[buy_price])
            else:
                buy_price = current

            current += 1

        return profit


arr = [7, 6, 4, 3, 1]
obj = Solution()
print(obj.max_profit(arr))
