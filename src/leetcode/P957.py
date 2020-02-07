import copy


class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        n = 8

        def index(c):
            r = 0
            for i in range(n):
                r = (r << 1) + c[i]
            return r

        d = {}
        r = {}
        p = -1
        s = -1
        for i in range(N):
            ind = index(cells)
            if ind not in d:
                d[ind] = i
                r[i] = copy.deepcopy(cells)
            else:
                p = i - d[ind]
                s = d[ind]
                break

            new_cells = copy.deepcopy(cells)
            new_cells[0] = 0
            new_cells[n - 1] = 0
            for j in range(1, n - 1):
                if cells[j - 1] != cells[j + 1]:
                    new_cells[j] = 0
                else:
                    new_cells[j] = 1
            cells = new_cells

        if s == -1 or p == 0:
            return cells
        else:
            N = (N - s) % p + s
            return r[N]


if __name__ == '__main__':
    print(Solution().prisonAfterNDays([1,0,0,1,0,0,1,0], 16))