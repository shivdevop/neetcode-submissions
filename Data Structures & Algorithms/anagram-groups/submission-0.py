from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map=defaultdict(list)

        for word in strs:
            count=[0]*26

            for c in word:
                ind=ord('z')-ord(c)
                count[ind]+=1
            word_map[tuple(count)].append(word)

        return list(word_map.values())        
        