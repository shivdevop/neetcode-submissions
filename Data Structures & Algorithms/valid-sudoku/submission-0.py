from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set=defaultdict(set)
        col_set=defaultdict(set)
        grid_set=defaultdict(set)

        r=len(board)
        c=len(board[0])

        for i in range(r):
            for j in range(c):
                if board[i][j]=='.':
                    continue
                val=board[i][j]
                if val in row_set[i] or val in col_set[j] or val in grid_set[(i//3,j//3)]:
                    return False

                row_set[i].add(val)
                col_set[j].add(val)
                grid_set[(i//3,j//3)].add(val)

        return True               

        