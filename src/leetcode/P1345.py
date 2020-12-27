from collections import defaultdict


class Solution:
    def minJumps(self, arr):
        n = len(arr)
        d = defaultdict(lambda: [])
        for i in range(n):
            d[arr[i]].append(i)
        q = [n - 1]
        f = {n - 1: 0}
        h, t = -1, 0
        while h < t:
            h += 1
            c = q[h]
            s = f[c]
            if c - 1 >= 0 and c - 1 not in f:
                f[c - 1] = s + 1
                q.append(c - 1)
                t += 1
            if c + 1 < n and c + 1 not in f:
                f[c + 1] = s + 1
                q.append(c + 1)
                t += 1
            for i in d[arr[c]]:
                if i == c:
                    continue
                if i in f:
                    break
                f[i] = s + 1
                q.append(i)
                t += 1
            if 0 in f:
                return f[0]
        return -1


# For test only
SI = (([100, -23, -23, 404, 100, 23, 23, 23, 3, 404],), ([7],), ([7, 6, 9, 6, 9, 6, 9, 7],), ([6, 1, 9],),
      ([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13],))
SO = (3, 0, 1, 2, 3)
TM = 'minJumps'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
