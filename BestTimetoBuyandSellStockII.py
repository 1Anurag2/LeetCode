from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
    

    
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')
#         max_profit = 0
#         profit = 0
#         for price in prices:
#             if(price < min_price):
#                 min_price = price
#             elif(price - min_price > profit):
#                 profit = price - min_price
#             elif(price < profit):
#                 min_price = price
#             elif(price - min_price > max_profit):
#                 max_profit = price - min_price
#         return (profit + max_profit)


