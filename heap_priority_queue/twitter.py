import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweet = {}
        self.user_followed = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet[userId] = self.user_tweet.get(userId, [])
        heapq.heappush(self.user_tweet[userId], [self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweet = []
        if userId in self.user_followed:
            for followedId in self.user_followed[userId]:
                print(userId, followedId)
                if followedId in self.user_tweet:
                    for tweet in self.user_tweet[followedId]:
                        heapq.heappush(all_tweet, tweet)
        if userId in self.user_tweet:
            for tweet in self.user_tweet[userId]:
                heapq.heappush(all_tweet, tweet)
        res = []
        #print(all_tweet)
        while all_tweet and len(res) < 10:
            res.append(heapq.heappop(all_tweet)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followed[followerId] = self.user_followed.get(followerId, [])
        if followeeId in self.user_followed[followerId]:
            return
        self.user_followed[followerId].append(followeeId)
        print(self.user_followed)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followed:
            self.user_followed[followerId].remove(followeeId)