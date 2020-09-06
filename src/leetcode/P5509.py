class Solution:
    def minCost(self, s, cost):
        n = len(s)
        r = 0
        s += '$'
        l = 0
        for i in range(n):
            if s[i + 1] != s[i]:
                if i - l + 1 > 1:
                    r += sum(cost[l: i + 1]) - max(cost[l: i + 1])
                l = i + 1
        return r


if __name__ == '__main__':
    print(Solution().minCost(s="aabaa", cost=[1, 2, 3, 4, 1]))
