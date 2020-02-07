import collections


class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d = collections.defaultdict(lambda: 0)
        for l in secret:
            d[l] += 1
        c = 0
        for l in guess:
            d[l] -= 1
            if d[l] >= 0:
                c += 1
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
        c -= b
        return '{}A{}B'.format(b, c)


if __name__ == '__main__':
    print(Solution().getHint('1123', '0111'))
