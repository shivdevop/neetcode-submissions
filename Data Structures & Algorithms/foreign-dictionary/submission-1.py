from collections import deque,defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph=defaultdict(list)
        
        #find the total number of chars 
        uniquechar= set("".join(words))
        uniquecharindex=[ord(c)-ord('a') for c in uniquechar]
      
        
        def compare(str1, str2):
            j = min(len(str1), len(str2))
            for i in range(j):
                if str1[i] != str2[i]:
                    ind1 = ord(str1[i]) - ord('a')
                    ind2 = ord(str2[i]) - ord('a')
                    graph[ind1].append(ind2)
                    return True  # Found a valid ordering relationship
            
            # If we reach here, one string is a prefix of the other
            # In lexicographic order, shorter string should come first
            if len(str1) > len(str2):
                return False  # Invalid: longer string comes before shorter
            return True  # Valid: shorter comes before longer (or they're equal)
        
        # Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            if not compare(words[i], words[i + 1]):
                return ""  # Invalid dictionary order
        #compare function will help us build the adjacency list
        #once the adjacency list is build, we will try to build topo sort ordering !!!
        
        indegree=[0]*26
        for node in uniquecharindex:
            for neighbor in graph[node]:
                indegree[neighbor]+=1
        
        queue=deque()
        
        for i in uniquecharindex:
            if indegree[i]==0:
                queue.append(i)
        
        count=0
        res=""
        while queue:
            node=queue.popleft()
            res+=chr(ord('a')+node)
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        
        if len(res)==len(uniquechar):
            return res
        return ""    
                    

        