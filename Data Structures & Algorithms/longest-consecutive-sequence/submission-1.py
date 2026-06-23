class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set=set(nums)
        longest=1

        for x in hash_set:
            if x-1 not in hash_set:
                curr=1
                while x+1 in hash_set:
                    curr+=1
                    x+=1
                    longest=max(longest,curr)
        return longest            
        
        