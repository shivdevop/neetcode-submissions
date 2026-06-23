class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_buy=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-min_buy
            max_profit=max(max_profit,profit)
            min_buy=min(min_buy,prices[i])
   
        return max_profit    
        