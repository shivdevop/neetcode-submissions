class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        temp=[]
        nums.sort()
        def dfs(ind):
          
            result.append(temp[:])

            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                dfs(i+1)
                temp.pop()    


        

        dfs(0)
        
        return result