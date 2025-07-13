class Solution(object):

    def nomnom(self, piles, k):

        ttl_hours = 0

        for pile in piles:
            ttl_hours += math.ceil(float(pile) / k)
        
        return ttl_hours

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        l, r = 1, max(piles)
        k = 0

        while l <= r:

            piv = (l+r)//2

            ttl_hours = self.nomnom(piles, piv)

            if ttl_hours > h:
                l = piv + 1
            else:
                r = piv - 1
                k = piv
        
        return k