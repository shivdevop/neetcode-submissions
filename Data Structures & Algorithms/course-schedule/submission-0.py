from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #we need a queue to start somewhere and an indegree array 
        #we are going to implement Kahn algo of topo sort using bfs method 
        
        #first lets prepare the adj list
        
        graph=defaultdict(list)

        for u,v in  prerequisites:
            graph[v].append(u)

        indegree=[0]*numCourses

        for i in range(numCourses):
            for nei in graph[i]:   
                indegree[nei]+=1

        queue=deque()        
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        count=0
        while queue:
            node=queue.popleft()
            count+=1

            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        return count==numCourses         
