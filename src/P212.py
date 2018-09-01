DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


class Solution:
    n = 0
    m = 0
    board = []
    visit = []
    dic = {}

    def doFind(self, word, x, y, index):
        if index >= len(word):
            return True

        for i in range(4):
            tx = x + DX[i]
            ty = y + DY[i]
            if 0 <= tx < self.n and 0 <= ty < self.m and not self.visit[tx][ty] and word[index] == self.board[tx][ty]:
                self.visit[tx][ty] = True
                if self.doFind(word, tx, ty, index + 1):
                    return True
                self.visit[tx][ty] = False
        return False

    def findWord(self, word):
        self.visit = []
        for i in range(self.n):
            self.visit.append([False] * self.m)
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == word[0]:
                    self.visit[i][j] = True
                    if self.doFind(word, i, j, 1):
                        return True
                    self.visit[i][j] = False
        return False

    def findWords(self, board, words):
        self.n = len(board)
        if self.n == 0:
            return []
        self.m = len(board[0])
        self.board = board
        ret = []
        dup = {}
        for word in words:
            if word not in dup and self.findWord(word):
                ret.append(word)
            dup[word] = True
        return ret

if __name__ == '__main__':
    print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
