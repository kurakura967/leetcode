import heapq
from collections import defaultdict

# Problem that could not be answered correctly
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # {userId: [[count, tweetId], [count, tweetId], ...]}
        self.followMap = defaultdict(set) # {userId: {followeeId, followeeId, ...}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                min_heap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


if __name__ == '__main__':
    # Your Twitter object will be instantiated and called as such:
    obj = Twitter()
    userId = 1
    tweetId = 5
    obj.postTweet(userId, tweetId)
    param_2 = obj.getNewsFeed(userId)

    followerId = 1
    followeeId = 2

    obj.follow(followerId, followeeId)
    obj.unfollow(followerId, followeeId)
