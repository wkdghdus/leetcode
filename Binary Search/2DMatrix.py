class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        h, w = len(matrix), len(matrix[0])
        l, r = 0, (h * w) - 1

        while l <= r:
            
            pivot = (l + r) // 2

            pivotW = pivot % w
            pivotH = pivot // w
            
            if matrix[pivotH][pivotW] < target:
                l = pivot + 1
            elif matrix[pivotH][pivotW] > target:
                r = pivot - 1
            elif matrix[pivotH][pivotW] == target:
                return True
            
        return False
