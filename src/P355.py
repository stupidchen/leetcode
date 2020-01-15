from collections import defaultdict, namedtuple


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(lambda: {})
        self.post = defaultdict(lambda: [])
        self.time = 0
        self.tweet = namedtuple('tweet', ['id', 'time'])

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.time += 1
        self.post[userId].append(self.tweet(id=tweetId, time=self.time))

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweet = []
        self.followers[userId][userId] = 1
        for user in self.followers[userId]:
            tweet.extend(self.post[user])
        sorted_tweet = sorted(tweet, key=lambda t: t.time, reverse=True)
        return list(map(lambda t: t.id, sorted_tweet[: 10]))

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId][followeeId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        try:
            del self.followers[followerId][followeeId]
        except Exception:
            pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))
