class Solution:
    def climbStairs(self, n: int) -> int:
        prev=1
        curr=2
        if n==1 or n==2:
            return n

        for i in range(2,n):
            temp=curr+prev
            prev=curr
            curr=temp

        return curr        
        