 def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash = {}

        for i in range(len(nums)):

            if target - nums[i] in hash:
                return [i, hash[target - nums[i]]]
            
            hash.update({nums[i]: i})

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             lst = [i, j]
        #             return lst