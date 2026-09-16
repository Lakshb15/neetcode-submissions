class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        minHeap = []

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                count, tweetId = self.tweetMap[followeeId][-1]
                index = len(self.tweetMap[followeeId]) - 1
                heapq.heappush(minHeap, [count, tweetId, followeeId, index])

        res = []

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index > 0:
                count, tweetId = self.tweetMap[followeeId][index - 1]
                heapq.heappush(
                    minHeap,
                    [count, tweetId, followeeId, index - 1]
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)