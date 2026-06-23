class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #we can keep the first row and first col as tracker !!

        #so first we need a flag for first row and first col 

        rows=len(matrix)
        cols=len(matrix[0])
        flagrow,flagcol=0,0
        for i in range(cols):
            if matrix[0][i]==0:
                flagrow=1
                break

        for i in range(rows):
            if matrix[i][0]==0:
                flagcol=1
                break      

        #now lets use the firstrow and firstcol as markers 

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0    

        if flagrow==1:
            for i in range(cols):
                matrix[0][i]=0

        if flagcol==1:
            for i in range(rows):
                matrix[i][0]=0

                                       

        
        