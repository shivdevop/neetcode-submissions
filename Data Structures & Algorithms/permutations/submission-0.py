class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        temp=[]
        taken=[-1 for _ in range(len(nums))]

        def dfs():
            if len(temp)==len(nums):
                result.append(temp[:])

            for i in range(len(nums)):
                if taken[i]==-1:
                    #we can take this
                    temp.append(nums[i])
                    taken[i]=1
                    dfs()
                    temp.pop()
                    taken[i]=-1




        dfs()
        return result    
        