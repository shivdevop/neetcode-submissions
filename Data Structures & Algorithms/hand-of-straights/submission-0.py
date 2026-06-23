from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count=Counter(hand)
        sorted_count=dict(sorted(count.items(),key=lambda x:x[0]))

        for key,freq in sorted_count.items():

            if freq>0:
                for i in range(groupSize):
                    if key+i not in sorted_count:
                        return False
                    elif key+i in sorted_count and sorted_count[key+i]<freq:
                        return False

                    sorted_count[key+i]-=freq

        return True                     
        
