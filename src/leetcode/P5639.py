class Solution:
    def minimumTimeRequired(self, jobs, k):
        w = [0] * k
        jobs = sorted(jobs, key=lambda x: -x)
        n = len(jobs)
        for i in range(n):
            w[i % k] += jobs[i]
        r = [max(w)]
        w = [0] * k
        c = {}

        def find(x, m):
            t = tuple(sorted(w))
            if t in c:
                return
            c[t] = True

            if x == n:
                r[0] = m
                return

            j = jobs[x]
            for i in range(k):
                t = max(w[i] + j, m)
                if t < r[0]:
                    w[i] += j
                    find(x + 1, t)
                    w[i] -= j

        find(0, 0)
        return r[0]


if __name__ == '__main__':
    print(Solution().minimumTimeRequired([254, 256, 256, 254, 251], 5))
    print(Solution().minimumTimeRequired([254, 256, 256, 254, 251, 256, 254, 253, 255, 251, 251, 255, 250, 257], 12))
