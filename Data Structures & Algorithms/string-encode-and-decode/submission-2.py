class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            j=i
            #the string length not necessarily will be a single digit character, so we need to move j
            #till our delimeter that we have set
            while(s[j]!="#"):
                j+=1
            string_len=int(s[i:j])
            res.append(s[j+1:j+1+string_len])
            i=j+1+string_len
        return res    
