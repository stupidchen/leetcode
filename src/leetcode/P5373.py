class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        l1, l2 = 1, 1
        d = {1}
        while l1 + l2 <= k:
            t = l1 + l2
            d.add(t)
            l1 = l2
            l2 = t

        d = sorted(d, reverse=True)
        r = 0
        for i in range(len(d)):
            c = k // d[i]
            r += c
            k = k % d[i]
            if k == 0:
                break
        return r


if __name__ == '__main__':
    print(Solution().findMinFibonacciNumbers(10 ** 9))
