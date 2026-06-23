class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]


        def dfs(nums,index,sum,temp):
            if sum>target:
                return 
            if index>=len(nums):
                if sum==target:
                    result.append(temp[:])
                return

            if nums[index]<=(target-sum):
                temp.append(nums[index])
                dfs(nums,index,sum+nums[index],temp)

                #if we do the above operation, then while returning we will also pop it from here to try a different route !!
                temp.pop()
                dfs(nums,index+1,sum,temp)
            else:
                dfs(nums,index+1,sum,temp)



        
        dfs(nums,0,0,[])   
        return result

        
        