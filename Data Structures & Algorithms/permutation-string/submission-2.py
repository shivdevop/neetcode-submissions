class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=[0]*26 
        count2=[0]*26 
        l1=len(s1)
        for c in s1:
            count1[ord(c)-ord('a')]+=1
        
        l=0

        for r in range(len(s2)):
            count2[ord(s2[r])-ord('a')]+=1

            if r-l+1==l1:
                if count1==count2:
                    return True 
                count2[ord(s2[l])-ord('a')]-=1
                l+=1
            
        
        return False


        