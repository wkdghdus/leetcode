class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        negative = []
        positive = []

        for nums in nums:
            if nums < 0:
                negative.append(nums)
            else:
                positive.append(nums)
        
        negative.sort(reverse=True)
        positive.sort()

        nums = negative + positive
        nums = list(set(nums))

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