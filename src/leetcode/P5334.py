from collections import defaultdict


class TweetCounts:

    def __init__(self):
        self.t = defaultdict(lambda: [])

    def recordTweet(self, tweetName, time):
        self.t[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        b = 86400
        if freq == 'minute':
            b = 60
        elif freq == 'hour':
            b = 3600

        r = [0] * ((endTime - startTime) // b + 1)
        for c in self.t[tweetName]:
            if startTime <= c <= endTime:
                r[(c - startTime) // b] += 1
        return r


# This kind of input is not supported by tester temporarily
if __name__ == '__main__':
    tweetCounts = TweetCounts()
    tweetCounts.recordTweet("tweet3", 0)
    tweetCounts.recordTweet("tweet3", 60)
    tweetCounts.recordTweet("tweet3", 10)
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))
    tweetCounts.recordTweet("tweet3", 120)
    print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))
