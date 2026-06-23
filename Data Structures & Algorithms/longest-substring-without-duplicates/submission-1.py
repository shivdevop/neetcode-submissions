from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left=0
        char_map=defaultdict(int) #we will store the indexes of the char
        longest=1
        for right in range(len(s)):
            #basically if new char is already in curr window
            if s[right] in char_map and char_map[s[right]]>=left:
                left=char_map[s[right]]+1
            longest=max(longest,right-left+1)
            char_map[s[right]]=right
        return longest        
        