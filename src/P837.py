class Solution:
    def new21Game(self, N, K, W):
        f = [0.0 for i in range(K + W)]
        f[0] = 1.0
        for i in range(1, K + W):
            t = 0
            if i - W > 0:
                t = f[i - W - 1]
            f[i] = f[i - 1] + (f[i - 1] - t) / W
            if i > K:
                f[i] -= (f[i - 1] - f[K - 1]) / W

        if f[K + W - 1] - f[K - 1] != 0:
            return (f[N] - f[K - 1]) / (f[K + W - 1] - f[K - 1])
        else:
            return 1.0