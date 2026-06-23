from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #we can use prims algo here, first we should build a graph list
        #take a visited and min heap array 

        #assume coordinates as points !!
        graph=defaultdict(list)
        n=len(points)
        for i in range(n):
            for j in range(i+1,n):
                x1,x2=points[i][0],points[j][0]
                y1,y2=points[i][1],points[j][1]
                edge_weight=abs(x1-x2)+abs(y1-y2)
                graph[i].append((j,edge_weight))
                graph[j].append((i,edge_weight))

        visited=set()
        sum=0
        #we can push a starting point in min_heap
        min_heap=[(0,0,-1)] #we can keep dist node parent        
        
        while min_heap:
            edge_wt,node,parent=heapq.heappop(min_heap)
            if node in visited:
                continue 

            visited.add(node)

            # if parent!=-1:
            #     res.append((parent,node))  

            sum+=edge_wt
            for neighbor in graph[node]:
                nei_node,nei_dist=neighbor 
                if nei_node not in visited:
                    heapq.heappush(min_heap,(nei_dist,nei_node,node))


        return sum        