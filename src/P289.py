import copy

d = [-1, 0, 1]

def count_neighbor(board, x, y, n, m):
    ret = 0
    for i in d:
        for j in d:
            if i != 0 or j != 0:
                tx, ty = x + i, y + j
                if 0 <= tx < n and 0 <= ty < m:
                    ret += board[tx][ty]
    return ret


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        tmp = copy.deepcopy(board)
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                t = count_neighbor(tmp, i, j, n, m)
                if tmp[i][j] == 1:
                    board[i][j] = 1 if t == 2 or t == 3 else 0
                else:
                    board[i][j] = 1 if t == 3 else 0


if __name__ == '__main__':
    print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
