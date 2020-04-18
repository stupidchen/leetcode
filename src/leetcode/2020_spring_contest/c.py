def larger(x, y):
    return x[0] >= y[0] and x[1] >= y[1] and x[2] >= y[2]


class Solution:
    def getTriggerTime(self, increase, requirements):
        f = [[0, 0, 0]] + increase
        n, m = len(increase), len(requirements)
        for i in range(1, n + 1):
            for j in range(3):
                f[i][j] = f[i - 1][j] + increase[i - 1][j]

        r = [-1] * m
        for i in range(m):
            ll, rr = 0, n + 1
            req = requirements[i]
            while ll < rr:
                mid = (ll + rr) // 2
                if larger(f[mid], req):
                    rr = mid
                else:
                    ll = mid + 1
            if ll <= n:
                r[i] = ll
        return r


if __name__ == '__main__':
    print(Solution().getTriggerTime(increase=[[1, 1, 1]], requirements=[[0, 0, 0]]))
