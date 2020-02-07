class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        n = len(graph)
        f = [-1] * n
        m = len(initial)
        s = [0] * m
        for i in range(m):
            if f[initial[i]] != -1:
                s[f[initial[i]]] = 1
                s[i] = 1
                continue
            f[initial[i]] = i
            q = [initial[i]]
            h = 0
            t = 1
            while h < t:
                s[i] += 1
                for j in range(n):
                    if graph[q[h]][j] == 1 and f[j] == -1:
                        f[j] = i
                        q.append(j)
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
    print(Solution().minMalwareSpread([[1,0,0,0,1,0,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,1,0,0,0],[0,0,0,1,1,0,0,0],[1,0,1,1,1,0,0,1],[0,1,0,0,0,1,0,0],[0,0,0,0,0,0,1,1],[0,0,0,0,1,0,1,1]], [7, 2]))
