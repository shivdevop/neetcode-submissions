class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]

        candidates.sort()
        
        def dfs(ind,target,temp):
            if target==0:
                result.append(temp[:])

            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break

                temp.append(candidates[i])
                dfs(i+1,target-candidates[i],temp)
                temp.pop()



        
        temp=[]
        dfs(0,target,temp)
        return result
        