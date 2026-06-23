import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.follows=defaultdict(set) #every key(userid) will have a set of userid it follows 

    def postTweet(self, userId: int, tweetId: int) -> None: 
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #generate latest 10 news for user with given userId's news feed
        users=set(self.follows[userId])
        users.add(userId)
        
        min_heap=[]

        for userid in users:
            for tweet in self.tweets[userid][-10:]:
                heapq.heappush(min_heap,tweet)
                if len(min_heap)>10:
                    heapq.heappop(min_heap)

        #now minheap will have latest 10 tweets:
        res=[]
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res[::-1]                

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.follows[followerId].discard(followeeId)
