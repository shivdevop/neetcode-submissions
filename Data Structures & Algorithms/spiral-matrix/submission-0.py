class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        cols=len(matrix[0])
        startrow,startcol,endrow,endcol=0,0,rows-1,cols-1
        res=[]
        while startrow<=endrow and startcol<=endcol:
            for i in range(startcol,endcol+1):
                res.append(matrix[startrow][i])

            for i in range(startrow+1,endrow+1):
                res.append(matrix[i][endcol])

            if startrow<endrow:
                for i in range(endcol-1,startcol-1,-1):
                    res.append(matrix[endrow][i])

            if startcol<endcol:
                for i in range(endrow-1,startrow,-1):
                    res.append(matrix[i][startcol])

            startrow+=1
            startcol+=1
            endrow-=1
            endcol-=1


        return res                            

