import collections


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(v, c ^ 1) for v in graph[node])

        return all(dfs(node) for node in range(1, N + 1) if node not in color)


if __name__ == '__main__':
    print(Solution().possibleBipartition(10, [[1, 2], [1, 3], [1, 4], [1, 5], [1, 8], [1, 6], [1, 9], [1, 7], [1, 10]]))
