class Solution:
    def rankTeams(self, votes):
        n = len(votes)
        if n == 0:
            return ''
        m = len(votes[0])

        r = {}
        for vote in votes:
            for t in range(m):
                if vote[t] not in r:
                    r[vote[t]] = [0] * (m + 1)
                    r[vote[t]][m] = -ord(vote[t])
                r[vote[t]][t] += 1

        sr = sorted(r.values(), reverse=True)
        ret = ''
        for r in sr:
            ret += chr(-r[m])
        return ret


# For test only
SI = ((["ABC", "ACB", "ABC", "ACB", "ACB"],),)
SO = ("ACB",)
TM = 'rankTeams'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
