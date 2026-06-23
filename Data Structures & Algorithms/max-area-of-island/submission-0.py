class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #basically we need to find number of pieces in each island and keep computing the largest island !!!!
        rows=len(grid)
        cols=len(grid[0])

        visited=[[0]*cols for _ in range(rows)]
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]

        def dfs(row,col):

            area=1
            for i in range(4):
                new_row=row+dr[i]
                new_col=col+dc[i]

                if 0<=new_row<rows and 0<=new_col<cols and visited[new_row][new_col]==0 and grid[new_row][new_col]==1:
                    visited[new_row][new_col]=1
                    area+=dfs(new_row,new_col)
            return area        
        
        max_area=0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==0 and grid[i][j]==1:
                    visited[i][j]=1
                    max_area=max(max_area,dfs(i,j))

        return max_area        
        
        