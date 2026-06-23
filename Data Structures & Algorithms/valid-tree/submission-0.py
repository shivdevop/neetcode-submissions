from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree of n nodes should have n-1 edges/ acyclic 
        #only one component 

        if len(edges)!=n-1:
            return False
        
        graph=defaultdict(list)

        for edge in edges:
            u,v=edge[0],edge[1]
            graph[u].append(v)
            graph[v].append(u)


        visited=set()
        def dfs(node):
            visited.add(node)

            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)



        flag=0
        for i in range(n):
            if i not in visited:
                if flag==1:
                    return False
                elif flag==0:
                    flag=1
                    dfs(i)

        return True            

        