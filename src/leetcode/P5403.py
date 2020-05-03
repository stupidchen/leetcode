import heapq


class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)
        m = len(mat[0])
        r = sum([mat[i][0] for i in range(n)])
        q = [(0, ) * n]
        v = set(q[0])
        h = [-r]
        head = 0
        while head < len(q):
            f = q[head]
            s = sum([mat[i][f[i]] for i in range(n)])
            for j in range(n):
                if f[j] + 1 < m:
                    t = s - mat[j][f[j]] + mat[j][f[j] + 1]
                    tf = [i for i in f]
                    tf[j] += 1
                    tp = tuple(tf)
                    if tp not in v:
                        if len(h) < k:
                            heapq.heappush(h, -t)
                            q.append(tp)
                            v.add(tp)
                        elif -h[0] > t:
                            heapq.heappop(h)
                            heapq.heappush(h, -t)
                            q.append(tp)
                            v.add(tp)
            head += 1
        return -h[0]


if __name__ == '__main__':
    print(Solution().kthSmallest(mat=[[1, 3, 11], [2, 4, 6]], k=9))
    print(Solution().kthSmallest(mat=[[1, 3, 11], [2, 4, 6]], k=5))
    print(Solution().kthSmallest(mat=[[1, 1, 10], [2, 2, 9]], k=7))
    print(Solution().kthSmallest(mat=[[1, 10, 10], [1, 4, 5], [2, 3, 6]], k=7))
    print(Solution().kthSmallest(mat=[[1, 10, 10], [1, 4, 5], [2, 3, 6]], k=14))
