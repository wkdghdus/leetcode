class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = list(set(nums)) # remove duplicates
        negative = []
        positive = []

        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        
        negative.sort()
        positive.sort()

        nums = negative + positive


        next = 0
        longest = 0
        curr = 0
        for num in nums:
            
            if num == next:
                curr += 1
            else:
                curr = 1
            
            longest = max(longest, curr)

            next = num + 1
        
        return longest