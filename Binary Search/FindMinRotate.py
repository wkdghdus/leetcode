class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]


        l, r = 0, len(nums) - 1

        while l <= r:
            piv = (l+r) // 2

            if nums[piv + 1] < nums[piv]:
                return nums[piv + 1]
            
            if nums[piv] < nums[piv-1]:
                return nums[piv]

            if nums[piv] > nums[r]:
                l = piv + 1
            else:
                r = piv - 1