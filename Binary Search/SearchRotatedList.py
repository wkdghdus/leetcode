class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1

        res = -1

        while l <= r:

            piv = (l+r) // 2

            if nums[piv] == target:
                res = piv
                break

            if nums[piv] > target:
                
                # if target is not in between l <-> piv
                # since there is no rotation point in between target < nums[l] <= nums[piv] 
                if nums[l] > target and nums[l] <= nums[piv]:
                    l = piv + 1
                # if target is in between l <-> piv
                else: 
                    r = piv - 1

            elif nums[piv] < target:

                # if target is not in between piv <-> r
                # since there is no rotation point in between nums[piv] <= nums[r] < target
                if nums[r] < target and nums[r] >= nums[piv]:
                    r = piv - 1
                # if target is in between piv <-> r
                else:
                    l = piv + 1


        return res
    

