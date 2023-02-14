class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        ttlLength = len(nums1) + len(nums2)
        num1Ind = 0
        num2Ind = 0
        val = 0.0

        if ttlLength % 2 == 1:
            for i in range(int(ttlLength/2+1)):
                if nums1[num1Ind] > nums2[num2Ind]:
                    val = nums1[num1Ind]
                    num1Ind += 1

                else:
                    val = nums2[num2Ind]
                    num2Ind += 1
        else:
            for i in range(int(ttlLength/2+1)):
                if nums1[num1Ind] > nums2[num2Ind]:
                    num1Ind += 1
                else:
                    num2Ind += 1
                
                if nums1[num1Ind+1]<nums2[num2Ind]:
                    val = (nums1[num1Ind] + nums1[num1Ind+1])/2
                elif nums1[num1Ind]>nums2[num2Ind+1]:
                    val = (nums2[num2Ind] + nums2[num2Ind+1])/2
                else:
                    val = (nums1[num1Ind]+nums2[num2Ind])/2
                
        
        return float(val)
        
            