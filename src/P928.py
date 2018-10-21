class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        n = len(graph)
        m = len(initial)
        s = [0] * m
        for i in range(m):
            s[i] = n
            q = [v for v in initial if v != initial[i]]
            v = [False] * n
            for v0 in initial:
                v[v0] = True
            h = 0
            t = m - 1
            while h < t:
                s[i] -= 1
                for j in range(n):
                    if graph[q[h]][j] == 1 and not v[j]:
                        q.append(j)
                        v[j] = True
                        t += 1
                h += 1
        ret = initial[0]
        maxs = s[0]
        for i in range(1, m):
            if s[i] > maxs or (s[i] == maxs and initial[i] < ret):
                ret = initial[i]
                maxs = s[i]
        return ret


if __name__ == '__main__':
    print(Solution().minMalwareSpread([[1,0,0,0,1],[0,1,1,0,0],[0,1,1,0,0],[0,0,0,1,0],[1,0,0,0,1]], [4]))