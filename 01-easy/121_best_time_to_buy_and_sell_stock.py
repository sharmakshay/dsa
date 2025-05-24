class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = 1000000
        for price in prices:
            if price < min_price:
                min_price = price

            max_profit = max(max_profit, price - min_price)

        return max_profit


test_cases = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]

for test_case in test_cases:
    print(Solution().maxProfit(test_case))
