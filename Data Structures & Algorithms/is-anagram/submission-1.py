class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_map1=[0]*26
        freq_map2=[0]*26
        for c in s:
            ind=ord('z')-ord(c)
            freq_map1[ind]+=1
        for c in t: 
            ind=ord('z')-ord(c)
            freq_map2[ind]+=1
        for c in t:
            ind=ord('z')-ord(c)
            if freq_map1[ind]!=freq_map2[ind]:
                return False
        return True               
        