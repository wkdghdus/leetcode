class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #using hash table
        table = {}

        #create a hash table with the key being the number and the value being the index
        for i in range(len(nums)):
            if target - nums[i] in table:
                return [i, table[target - nums[i]]]
            else:
                table[nums[i]] = i

        #brute force method
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]