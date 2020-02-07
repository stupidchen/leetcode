class Worker:
    def __init__(self, q, w):
        self.q = q
        self.w = w
        self.p = w / q


class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        n = len(quality)
        w = []
        for i in range(n):
            w.append(Worker(quality[i], wage[i]))
        w.sort(key=lambda x: x.p)
        s = [0]
        for i in range(n):
            if i >= K:
                s.append(s[i - K] + w[i].q - w[i - K].q)
            else:
                s[0] += w[i].q
        ret = s[n - K] * w[n - K].q
        for i in range(n - K + 1, n):
            if s[i] * w[i].q < ret:
                ret = s[i] * w[i].q
        return ret


if __name__ == "__main__":
    print(Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2))
