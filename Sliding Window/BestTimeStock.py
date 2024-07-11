class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        result = 0
        lowest = prices[0]

        for price in prices:
            if lowest > price:
                lowest = price
            result = max(result, price - lowest)
        
        return result