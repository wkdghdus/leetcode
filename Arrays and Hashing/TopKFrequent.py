class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

        # 2nd try using a hash table
        numsFreq = {}

        for num in nums:
            if num in numsFreq:
                numsFreq[num] += 1
            else:
                numsFreq[num] = 1

        ret = []

        frequency = numsFreq.values()
        number = numsFreq.keys()

        for i in range(k):
            maximum = frequency.index(max(frequency))
            ret.append(number[maximum])
            frequency[maximum] = 0
        
        return ret




        # 1st try - this code those not cover the case where there is a negative integer in the array
        # numsFreq = [0] * (max(nums)+1)

        # for num in nums:
        #     numsFreq[num] += 1
        
        # ret = []

        # for i in range(k):
        #     maximum = numsFreq.index(max(numsFreq))
        #     ret.append(maximum)
        #     numsFreq[maximum] = 0
        
        # return ret
            
        
