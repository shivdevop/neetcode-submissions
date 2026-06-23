class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #so the thing is we have to create partitions at all possible indexes and if the string is palindrome then we create a partition there
        result=[]
        temp=[]

        def ispalindrome(s):
            l=0
            r=len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True        

        def dfs(ind):
            if ind==len(s):
                result.append(temp[:])

            for i in range(ind,len(s)):
                sliced_word=s[ind:i+1]
                if ispalindrome(sliced_word):
                    temp.append(sliced_word)
                    dfs(i+1)
                    temp.pop()

        dfs(0)    
        return result
        