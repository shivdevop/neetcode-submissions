from collections import deque 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #two queues and two sets for getting which coordinates can reach the pacific and atlantic ocean and then we will take the
        #.. intersection of both the sets !!!

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        rows=len(heights)
        cols=len(heights[0])
        
        a_seen=set()
        a_queue=deque()
        
        p_seen=set()
        p_queue=deque()

        for i in range(cols):
            p_seen.add((0,i))
            p_queue.append((0,i))

        for i in range(rows):
            p_seen.add((i,0))
            p_queue.append((i,0))

        for i in range(cols):
            a_seen.add((rows-1,i))
            a_queue.append((rows-1,i))

        for i in range(rows):
            a_seen.add((i,cols-1))
            a_queue.append((i,cols-1))


        while p_queue:
            r,c=p_queue.popleft()

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc

                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in p_seen and heights[nr][nc]>=heights[r][c]:
                    p_queue.append((nr,nc))
                    p_seen.add((nr,nc))


        while a_queue:
            r,c=a_queue.popleft()

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc

                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in a_seen and heights[nr][nc]>=heights[r][c]:
                    a_queue.append((nr,nc))
                    a_seen.add((nr,nc))

        return list(p_seen & a_seen)            
                                 


