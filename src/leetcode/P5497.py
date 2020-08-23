from data_structure.treap import Treap


class Solution:
    def findLatestStep(self, arr, m):
        n = len(arr)
        if m == n:
            return n

        f = [0] * n
        for i in range(n):
            f[arr[i] - 1] = i + 1

        t = Treap()
        for i in range(m):
            t.add(f[i])
        p = t.max().v
        r = f[m] - 1 if f[m] > p else -1
        for i in range(m, n):
            l = f[i - m]
            t.remove(l)
            t.add(f[i])
            p = t.max().v
            if l > p:
                if i == n - 1:
                    r = max(r, l - 1)
                elif f[i + 1] > p:
                    r = max(r, min(l - 1, f[i + 1] - 1))

        return r


if __name__ == '__main__':
    print(Solution().findLatestStep([10, 6, 9, 4, 7, 8, 5, 2, 1, 3], 1))
    print(Solution().findLatestStep(arr=[3, 5, 1, 2, 4], m=1))
    print(Solution().findLatestStep(arr=[2, 1], m=2))
