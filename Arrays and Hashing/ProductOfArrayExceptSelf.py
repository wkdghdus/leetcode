# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1] * len(nums)

        prefix = 1

        for ind, num in enumerate(nums):
            ret[ind] = prefix
            prefix *= num
        
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= postfix
            postfix *= nums[i]
        
        return ret