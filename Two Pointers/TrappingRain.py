class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        #two pointer approach
        left, right = 0, len(height) - 1
        ttlArea = 0

        while left < right: 
            area = min(height[left], height[right]) * (right - left - 1)

            for bar in height[left+1:right]:
                area -= bar
            
            ttlArea += area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return ttlArea