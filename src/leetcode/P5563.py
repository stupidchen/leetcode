MOD = 10 ** 9 + 7


class Solution:
    def maxProfit(self, inventory, orders):
        a = sorted(inventory, reverse=True)
        a.append(0)
        n = len(a)
        i = 1
        r = 0
        t = 0
        while i < n:
            lt = t
            t += (a[i - 1] - a[i]) * i
            s = (min(orders, t) - lt) // i
            mm = (min(orders, t) - lt) % i
            ll = a[i - 1] - s + 1
            ss = (a[i - 1] + ll) * s // 2 * i % MOD
            r = (r + ss) % MOD
            if ll > 0:
                r = (r + (ll - 1) * mm) % MOD
            if t >= orders:
                break
            i += 1
        return r


if __name__ == '__main__':
    print(Solution().maxProfit([773160767], 252264991))
    print(Solution().maxProfit(inventory=[2, 5], orders=4))
    print(Solution().maxProfit(inventory=[2, 8, 4, 10, 6], orders=20))
