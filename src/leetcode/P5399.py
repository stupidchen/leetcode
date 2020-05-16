def larger(x, y):
    if y is None or len(x) > len(y):
        return True
    if len(x) < len(y):
        return False
    return x > y


class Solution:
    def largestNumber(self, cost, target):
        f = [None] * (target + 1)
        f[0] = ''
        for i in range(9):
            c = cost[i]
            k = chr(i + 49)
            for j in range(c, target + 1):
                if f[j - c] is not None:
                    t = k + f[j - c]
                    if larger(t, f[j]):
                        f[j] = t
        if f[target] is None:
            f[target] = '0'
        return f[target]


if __name__ == '__main__':
    print(Solution().largestNumber(cost=[6, 10, 15, 40, 40, 40, 40, 40, 40], target=47))
