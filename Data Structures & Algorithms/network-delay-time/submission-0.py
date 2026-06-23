import heapq 
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #we can implement djikstra or bellman ford here 

        #lets implement djikstra here 

        graph=defaultdict(list)

        for edge in times:
            u,v,dist=edge 
            graph[u].append((v,dist))

        #we can take dist array ofc and make source dist 0 and push it in min_heap

        maxi=float('inf')
        dist=[maxi]*(n+1)
        dist[k]=0
        min_heap=[(0,k)]   #dist,node

        #we can keep relaxing the dist
        while min_heap:            
            dist_node,node=heapq.heappop(min_heap)

            for neighbor in graph[node]:
                nei_node,dist_edge=neighbor 
                if dist_node+dist_edge < dist[nei_node]:
                    dist[nei_node]=dist_node+dist_edge
                    heapq.heappush(min_heap,(dist[nei_node],nei_node))

        min_time_taken=float('-inf')
        for i in range(1,n+1):
            if dist[i]==maxi:
                return -1
            min_time_taken=max(min_time_taken,dist[i])

        return min_time_taken        



                    
        