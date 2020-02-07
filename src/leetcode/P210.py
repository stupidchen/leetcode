class Solution:
    def findOrder(self, numCourses, prerequisites):
        edges = {}
        for i in range(numCourses):
            edges[i] = {}
        for pair in prerequisites:
            edges[pair[0]][pair[1]] = True
        visit = [False] * numCourses
        ret = []
        for i in range(numCourses):
            cur = None
            for j in range(numCourses):
                if not visit[j] and len(edges[j]) == 0:
                    cur = j
                    break
            if cur is None:
                return []
            ret.append(cur)
            visit[cur] = True
            for j in range(numCourses):
                if not visit[j] and cur in edges[j]:
                    del edges[j][cur]
        return ret
