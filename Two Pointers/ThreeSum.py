class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        ret = []

        for i, target in enumerate(nums):

            if target > 0:
                break
            
            if i > 0 and target == nums[i - 1]:
                continue
            
            low, high = i+1, len(nums) - 1

            while low < high:
                
                three_sum = target + nums[low] + nums[high]

                if three_sum > 0:
                    high -= 1
                elif three_sum < 0:
                    low += 1
                else:
                    ret.append([target, nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while nums[low] == nums[low-1] and low < high:
                        low += 1
                    
        return ret
            
        