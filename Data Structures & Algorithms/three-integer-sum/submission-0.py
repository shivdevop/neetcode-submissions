class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #make sure that you pick first element and then you do two pointer problem with some tweakings !!!

        res=[]
        nums.sort()

        for i,num in enumerate(nums):

            if i>0 and num==nums[i-1]:
                continue
            

            j=i+1
            k=len(nums)-1
            while j<k:
                target=num+nums[j]+nums[k]
                if target==0:
                    res.append([num,nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1

                elif target>0:
                    k-=1
                else:
                    j+=1
        return res


        
        