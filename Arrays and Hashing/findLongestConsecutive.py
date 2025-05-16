class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #remove duplicates
        nums_set = set(nums)

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:

                curr = num + 1
                streak = 1

                while curr in nums_set:
                    curr += 1
                    streak += 1
                
                longest = max(longest, streak)
        
        return longest

        # if nums == []:
        #     return 0

        # nums = list(set(nums)) # remove duplicates

        # nums.sort()

        # maximum = 1
        # counter = 1

        # curr = nums[0]

        # for nums in nums[1:]:
        #     if curr+1 == nums:
        #         counter += 1
        #         maximum = max(counter, maximum)

        #     else:
        #         counter = 1
            
        #     curr = nums
        
        # return maximum
            