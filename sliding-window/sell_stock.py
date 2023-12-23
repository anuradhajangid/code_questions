#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = prices[0]
        if len(prices) < 2:
            return 0
        for day in range(1,len(prices)):
            profit = prices[day] - minprice
            if profit > maxprofit:
                maxprofit = profit
            minprice = min(minprice, prices[day])
        return maxprofit


                
            
        