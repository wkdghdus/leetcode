class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        low = prices[0]
        maxProfit = 0

        for price in prices:
            if low > price:
                low = price
            
            maxProfit = max(maxProfit, price - low)
        
        return maxProfit