class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        d = []
        q = []
        for i in range(n):
            d.append([0] * (n + 1))
            q.append((quiet[i], i))
        for t in richer:
            d[t[0]][0] += 1
            d[t[0]][d[t[0]][0]] = t[1]
        q = sorted(q)

        ret = [-1] * n
        queue = [0] * n
        for k in range(n):
            i = q[k][1]
            h = 0
            t = 1
            queue[0] = i
            if ret[i] == -1:
                ret[i] = i
            while h < t:
                for j in range(1, d[queue[h]][0] + 1):
                    next = d[queue[h]][j]
                    if ret[next] == -1:
                        ret[next] = i
                        queue[t] = next
                        t += 1
                h += 1
        return ret