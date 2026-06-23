from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs multisource algo 
        #visited grid 
        #we will use a queue to push all the starting rotten oranges 
        rows=len(grid)
        cols=len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=grid

        queue=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j,0))
        

        time_taken=0
        while queue:
            row,col,time=queue.popleft()
            time_taken=max(time_taken,time)
            for dr,dc in directions:
                nr=row+dr
                nc=col+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and visited[nr][nc]!=2:
                    queue.append((nr,nc,time+1))
                    visited[nr][nc]=2

        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==1:
                    return -1

        return time_taken            

        