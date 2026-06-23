class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        last_end=float('-inf')
        min_removals=0
        for start,end in intervals:
            if start>=last_end:
                last_end=end
            else:
                min_removals+=1
        return min_removals        

        