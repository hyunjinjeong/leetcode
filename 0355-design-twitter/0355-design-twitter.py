class Twitter:
    # top 10 recent tweets는 heap 쓰면 되는데
    # follow, unfollow를 어떻게 구현하지?
    # 일단 간단하게 follower 목록을 다 돌면서 10개 뽑으면 되긴 함.
    # feed를 그때그때 생성할지 follow, unfollow 시점에 만들어둘지...
    # 일단 on demand로 가보자

    def __init__(self):
        self.time = 0
        self.tweets = collections.defaultdict(list) # user_id:(time, tweet_id)
        self.followers = collections.defaultdict(set) # user_id:followee_ids

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)

        # size가 10인 min heap을 유지하고, 마지막엔 거꾸로 정렬하면 됨. (어차피 n=10)
        min_heap = []
        for follower_id in self.followers[userId]:
            followee_tweet_ids = self.tweets[follower_id]
            for tweet_id in followee_tweet_ids:
                heapq.heappush(min_heap, tweet_id)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        
        return [tweet_id for time, tweet_id in sorted(min_heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)