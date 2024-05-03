class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ###second try
        #first sort the array
        nums.sort()

        #initialize the result array
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums)-1

            while left < right:
                sum = a + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return res
                

        ###first try but too slow!!!
        # #first sort the array
        # nums.sort()

        # #initialize the result array
        # res = []

        # for targetInd in range(len(nums)):
        #     left = targetInd + 1
        #     right = len(nums)-1

        #     while left < right:
        #         if nums[left] + nums[right] == nums[targetInd]*-1 and [nums[targetInd], nums[left], nums[right]] not in res:
        #             res.append([nums[targetInd], nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #         elif nums[left] + nums[right] < nums[targetInd]*-1:
        #             left += 1
        #         else:
        #             right -= 1
                
        # return res



        