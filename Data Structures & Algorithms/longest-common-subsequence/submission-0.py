class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[-1 for _ in range(n)]for _ in range(m)]

        def helper(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0

            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]

            matchh=0    
            if text1[ind1]==text2[ind2]:
                matchh=1+helper(ind1-1,ind2-1)

            nonmatch=max(helper(ind1-1,ind2),helper(ind1,ind2-1))
            dp[ind1][ind2]=max(matchh,nonmatch)
            return max(matchh,nonmatch)    
                    

        return helper(m-1,n-1)            
        