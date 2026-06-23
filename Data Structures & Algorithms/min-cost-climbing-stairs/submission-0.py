class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            return cost[-1]

        prev=cost[0]
        curr=cost[1]
        for i in range(2,len(cost)):
            temp=cost[i]+min(curr,prev)
            prev=curr
            curr=temp

        return min(prev,curr)
        