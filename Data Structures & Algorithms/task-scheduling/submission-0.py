from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map=defaultdict(int)
        max_freq=0
        for c in tasks:
            freq_map[c]+=1
            if freq_map[c]>max_freq:
                max_freq=freq_map[c]
                key=c

        idleintervals=(max_freq-1) * n    

        #very imp line, because basically we have already placed one max_freq char, we have to work it like that 
        del freq_map[key]

        for char,freq in freq_map.items():
            if freq==max_freq:
                idleintervals-=freq-1
                continue
            idleintervals-=freq

        min_cycles=len(tasks) + max(0,idleintervals)
        return min_cycles        
        