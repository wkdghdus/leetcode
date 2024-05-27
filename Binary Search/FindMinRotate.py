class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            
            #if the array is completely sorted with no rotation
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            piv = (l + r) // 2
            
            if nums[l] <= nums[piv]:
                l = piv + 1
            else:
                r = piv - 1

            res = min(nums[piv], res)
            
        
        return res