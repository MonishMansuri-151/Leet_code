# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set()for x in range(9)]
        columns= [set() for x in range(9)]
        grid = [set() for _ in range(3) for _ in range(3)]

        for x in range(9):
            for y in range(9):
                cell_value = board[x][y]
                if cell_value == ".":
                    continue
                box = (x // 3) * 3 + (y // 3)    
                if cell_value in rows[x] or cell_value in columns[y] or cell_value in grid [box]:
                    return False
                rows[x].add(cell_value)
                columns[y].add(cell_value)
                grid[box].add(cell_value)
        return True
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
obj = Solution()
print(obj.isValidSudoku(board))