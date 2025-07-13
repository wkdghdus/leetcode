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

            pivot_w = pivot % w 
            pivot_h = pivot // w

            if matrix[pivot_h][pivot_w] > target:
                r = pivot - 1
            elif matrix[pivot_h][pivot_w] < target:
                l = pivot + 1
            else:
                return True

        return False
