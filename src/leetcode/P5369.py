class Solution:
    def numTeams(self, rating):
        n = len(rating)
        r = 0
        for i in range(n):
            ll, lb, rl, rb = 0, 0, 0, 0
            for j in range(i):
                if rating[i] > rating[j]:
                    ll += 1
                elif rating[i] < rating[j]:
                    lb += 1
            for j in range(i + 1, n):
                if rating[i] > rating[j]:
                    rl += 1
                elif rating[i] < rating[j]:
                    rb += 1
            r += ll * rb + lb * rl
        return r


if __name__ == '__main__':
    print(Solution().numTeams([1, 2, 3, 4]))
