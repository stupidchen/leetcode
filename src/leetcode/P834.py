from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        v = defaultdict(lambda: set())
        for s, t in edges:
            v[s].add(t)
            v[t].add(s)
        depths = [0] * n
        subtree = [0] * n
        ret = [0] * n

        def traversal(node, parent, depth):
            r = 1
            depths[node] = depth
            for i in v[node]:
                if i != parent:
                    r += traversal(i, node, depth + 1)
            subtree[node] = r
            return r

        def calculate_distance(node, parent, distance):
            ret[node] = distance
            for i in v[node]:
                if i != parent:
                    calculate_distance(i, node, distance + (n - subtree[i]) - subtree[i])

        traversal(0, -1, 0)
        calculate_distance(0, -1, sum(depths))
        return ret


if __name__ == '__main__':
    print(Solution().sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
