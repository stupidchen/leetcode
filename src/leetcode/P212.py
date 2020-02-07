DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


class Trie:
    def __init__(self):
        self.next = {}
        self.val = False
        self.prefix = 0

    def insert(self, word):
        self.prefix += 1
        if len(word) == 0:
            self.val = True
            return
        if word[0] not in self.next:
            self.next[word[0]] = Trie()
        self.next[word[0]].insert(word[1:])


class Solution:
    n = 0
    m = 0
    board = []
    visit = []
    dic = {}
    ans = []

    def findWord(self, trie, x, y, word):
        trie = trie.next.get(self.board[x][y])
        if trie is None or trie.prefix == 0:
            return 0

        self.visit[x][y] = True
        hit = 0
        word += self.board[x][y]
        if trie.val:
            self.ans.append(word)
            hit += 1
            trie.val = False

        for i in range(4):
            tx = x + DX[i]
            ty = y + DY[i]
            if 0 <= tx < self.n and 0 <= ty < self.m and not self.visit[tx][ty]:
                hit += self.findWord(trie, tx, ty, word)

        self.visit[x][y] = False
        trie.prefix -= hit
        return hit

    def findWords(self, board, words):
        self.n = len(board)
        if self.n == 0:
            return []
        self.m = len(board[0])
        self.board = board
        root = Trie()
        for word in words:
            root.insert(word)

        self.visit = []
        for i in range(self.n):
            self.visit.append([False] * self.m)
        self.ans = []
        for i in range(self.n):
            for j in range(self.m):
                self.findWord(root, i, j, '')
        return self.ans


if __name__ == '__main__':
    print(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                               ["oath", "pea", "eat", "rain"]))
