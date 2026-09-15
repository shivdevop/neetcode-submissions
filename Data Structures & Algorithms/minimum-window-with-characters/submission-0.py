class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #need->freq of string t 
        need={}
        #window->our traversal window freq that we are counting !!
        window={}
        #have-> how many distinct character requirement is satisfied
        
        for ch in t:
            need[ch]=need.get(ch,0)+1
        
        required=len(need)
        have=0
        l=0
        result=""
        min_len=float("inf")

        for r in range(len(s)):
            ch=s[r]
            window[ch]=window.get(ch,0)+1

            #this char in window has reached its frequency according to what is needed
            if ch in need and window[ch]==need[ch]:
                have+=1

            while have==required:
                #update answer
                if r-l+1<min_len:
                    min_len=r-l+1
                    result=s[l:r+1]
                
                leftmost=s[l]
                window[leftmost]-=1

                if leftmost in need and window[leftmost]<need[leftmost]:
                    have-=1
                

                l+=1

        

        return result
            








        