class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if i<j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(rows):
            for j in range(0,cols//2):
                matrix[i][j],matrix[i][cols-1-j]=matrix[i][cols-1-j],matrix[i][j]

                            

        