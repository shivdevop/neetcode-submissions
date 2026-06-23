class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def dfs(nums,i,temp):
            if i>=len(nums):
                result.append(temp[:])
                return 

            #take and not take 
            temp.append(nums[i])
            dfs(nums,i+1,temp)
            temp.pop()
            dfs(nums,i+1,temp)




        dfs(nums,0,[])    
        return result
        