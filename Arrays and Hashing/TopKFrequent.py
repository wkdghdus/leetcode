class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = [[] for i in range(len(nums) + 1)] 

        for num in set(nums):
            ind = nums.count(num)
            freq[ind].append(num)
        
        print(freq)

        ret = []

        for ind in range(len(nums), 0, -1):
            if len(ret) >= k:
                break
            
            for num in freq[ind]:
                ret.append(num)
        
        return ret