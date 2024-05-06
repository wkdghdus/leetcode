class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        #two pointer approach
        left = 0 
        right = len(height) - 1
        maxArea = 0

        while left < right:

            currArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currArea)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea
