from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #we can track whatall cells are connected to the boundary 0s in horizontal and vertical directions !!!

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        rows=len(board)
        cols=len(board[0])

        queue=deque()
        for i in range(rows):
            for j in range(cols):
                if (i==0 or i==rows-1 or j==0 or j==cols-1) and board[i][j]=="O":
                    board[i][j]="T"
                    queue.append((i,j))
                    # visited.add((i,j))
                    #we actually dont need visited set here because we have updated the "O" to "T"

        while queue:
            r,c=queue.popleft()

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc

                if 0<=nr<rows and 0<=nc<cols and board[nr][nc]=="O":
                    board[nr][nc]="T"
                    queue.append((nr,nc))


        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="T":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"



        