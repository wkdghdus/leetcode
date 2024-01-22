class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in range(9):
            nums = []
            for column in range(9):
                if board[row][column] not in nums:
                    nums.append(board[row][column])
                else:
                    if board[row][column] != ".":
                        return False
            
        for column in range(9):
            nums = []
            for row in range(9):
                if board[row][column] not in nums:
                    nums.append(board[row][column])
                else:
                    if board[row][column] != ".":
                        return False
            
        for boxrow in range(0, 9, 3):
            for boxcolumn in range(0, 9, 3):
                nums = []
                for row in range(0, 3):
                    for column in range(0, 3):
                        if board[row+boxrow][column+boxcolumn] not in nums:
                            nums.append(board[row+boxrow][column+boxcolumn])
                        else:
                            if board[row+boxrow][column+boxcolumn] != ".":
                                return False
            
        return True
    