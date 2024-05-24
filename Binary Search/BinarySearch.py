class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums) - 1

        while l <= r: 

            piv = (l + r) // 2

            if nums[piv] < target: 
                l = piv + 1
            elif nums[piv] > target:
                r = piv - 1
            elif nums[piv] == target:
                return piv
            
        return -1