class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            pivot = (l + r) // 2
            totalTime = 0

            for pile in piles:
                totalTime += (pile // pivot) + (pile % pivot > 0)
            
            if totalTime > h: 
                l = pivot + 1
            elif totalTime <= h:
                r = pivot - 1
                k = pivot
            
        return k