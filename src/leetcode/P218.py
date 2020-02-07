import heapq


class Solution:
    def getSkyline(self, buildings):
        buildings.append([float('inf'), float('inf'), 0])

        bh = [(0, -float('inf'), -1)]  # (-height, -right, left)
        ret = []
        for b in buildings:
            r = -1
            while bh and -bh[0][1] < b[0]:
                tb = heapq.heappop(bh)
                r = max(r, -tb[1])
                if -bh[0][1] > r:
                    ret.append([r, -bh[0][0]])

            if bh and b[2] > -bh[0][0]:
                if ret and ret[-1][0] == b[0]:
                    ret[-1][1] = b[2]
                else:
                    ret.append([b[0], b[2]])

            if not bh or (b[2] > -bh[0][0] or b[1] > -bh[0][1]):
                heapq.heappush(bh, (-b[2], -b[1], b[0]))

        return ret


# For test only
SI = (([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],), ([[1, 2, 1], [1, 2, 2], [1, 2, 3]],))
SO = ([[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]], [[1, 3], [2, 0]])
TM = 'getSkyline'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
