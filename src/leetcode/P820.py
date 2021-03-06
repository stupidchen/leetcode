class Solution:
    def minimumLengthEncoding(self, words):
        root = {}

        def insert(word, index, node):
            if index >= len(word):
                return

            c = word[index]
            if c not in node:
                node[c] = {}
            insert(word, index + 1, node[c])

        ret = [0]

        def get_result(node, length):
            if node is None:
                return
            if len(node) == 0:
                ret[0] += length + 1
            else:
                for succ in node:
                    get_result(node[succ], length + 1)

        for w in words:
            insert(w[::-1], 0, root)
        get_result(root, 0)
        return ret[0]


if __name__ == '__main__':
    print(Solution().minimumLengthEncoding(['me', 'bell', 'time']))
