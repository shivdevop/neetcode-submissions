from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        r_set=defaultdict(set)
        c_set=defaultdict(set)
        grid_set=defaultdict(set)

        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                if (val in r_set[r]) or (val in c_set[c]) or (val in grid_set[(r//3,c//3)]):
                    return False
                
                r_set[r].add(val)
                c_set[c].add(val)
                grid_set[(r//3,c//3)].add(val)
        return True                
        