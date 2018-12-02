class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        d = sorted(deck)
        n = len(d)
        r = [0] * n
        t = [i for i in range(n)]
        j = 0
        while len(t) != 0:
            r[t[0]] = d[j]
            j += 1
            if len(t) > 1:
                t = t[2:] + [t[1]]
            else:
                t = t[1:]

        return r


if __name__ == '__main__':
    print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
