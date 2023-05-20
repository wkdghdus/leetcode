class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if (len(nums) != len(set(nums))):
            return True
        else:
            return False
        
        # alreadyIterated = set()    #list of numbers already iterated

        # #iterate through nums
        # for num in nums:
        #     if num in alreadyIterated:
        #         return True

        #     alreadyIterated.add(num)
        
        # return False
        