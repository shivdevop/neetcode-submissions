from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_map=defaultdict(list)

        for s in strs:
            hash_t=[0]*26
            for c in s:
                hash_t[ord(c)-ord('a')]+=1
            
            group_map[tuple(hash_t)].append(s)
        

        return list(group_map.values())


        