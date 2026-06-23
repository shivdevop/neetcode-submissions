class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # so we will create a board with dots and we will do dfs column wise and traverse over diff rows and push a queen and
        #then move to the next column , after dfs we will come back replace the placed queen with a dot and then move to next column 
        rows,cols=n,n
        board=[["." for _ in range(n)] for _ in range(n)]
        result=[]
        
        def fillPossible(row,col):
            duprow=row
            dupcol=col

            while row>=0 and col>=0:
                if board[row][col]=='Q':
                    return False
                row-=1
                col-=1

            row,col=duprow,dupcol
            while col>=0:
                if board[row][col]=='Q':
                    return False
                col-=1

            col=dupcol

            while col>=0 and row<rows:
                if board[row][col]=='Q':
                    return False
                row+=1
                col-=1

            return True       


        def dfs(c):
            if c==n:
                result.append(["".join(row) for row in board])
                return 

            #we will start filling for this particular column 
            for r in range(rows):
                if fillPossible(r,c):
                    board[r][c]="Q"
                    dfs(c+1)
                    board[r][c]="."   


        
        dfs(0)
        return result



        