class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #bellman ford mei we can relax the edges n-1 times but here we can make atmost k stops, so we can relax the edges k+1 times
        #k stops means k+1 edges 
        maxi=float('inf')
        dist=[maxi]*n
        dist[src]=0

        for i in range(k+1):
            temp=dist[:]
            for s,d,p in flights:
                if dist[s]==maxi:
                    continue
                elif dist[s]+p<temp[d]:
                    temp[d]=dist[s]+p
            dist=temp        

        return dist[dst] if dist[dst]!=maxi else -1                

