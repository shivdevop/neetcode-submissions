class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
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



        count=0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)

        return count            
        