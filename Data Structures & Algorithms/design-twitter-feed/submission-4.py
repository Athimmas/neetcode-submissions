class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time,tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        maxheap = []
        res = []

        self.followers[userId].add(userId)
        
        for followee in self.followers[userId]:
            if followee in self.tweets:
                m = self.tweets[followee]
                index = len(m) - 1
                time,tweetid = m[index]
                heapq.heappush(maxheap,[time,tweetid,followee,index-1])

        while maxheap and len(res) < 10:
            count,tweetid,followee,index = heapq.heappop(maxheap)
            res.append(tweetid)
            if index >= 0:
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(maxheap,[count,tweetId,followee,index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


        



