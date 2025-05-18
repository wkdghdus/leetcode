class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        low, high = 0, len(height) - 1
        max_water = 0

        while low < high:
            curr_water = min(height[low], height[high]) * (high - low)

            max_water = max(max_water, curr_water)

            if height[low] < height[high]:
                low += 1
            else:               
                high -= 1

                # note that if the height is the same, 
                # it is impossible to get a bigger area when you shift either index.
                # because the width is guaranteed to be shorter and the height will be the same or shorter.  
        
        return max_water
