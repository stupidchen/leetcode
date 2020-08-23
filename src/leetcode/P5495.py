class Solution:
    def mostVisited(self, n: int, rounds):
        f = [0] * n
        s = rounds[0] - 1
        for i in range(1, len(rounds)):
            while s != rounds[i] - 1:
                f[s] += 1
                s = (s + 1) % n
        f[s] += 1

        t = [(f[i], i + 1) for i in range(n)]
        t = sorted(t)
        return [q[1] for q in t if q[0] == max(f)]


if __name__ == '__main__':
    print(Solution().mostVisited(n=4, rounds=[1, 3, 1, 2]))
