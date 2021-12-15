from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        d = {}
        l = set()
        for word in words:
            r = d
            for c in word:
                if c not in r:
                    r[c] = {}
                r = r[c]
            l.add(word)

        ret = ['']

        def traversal(s, d):
            if len(s) > len(ret[0]):
                ret[0] = s

            for o in range(26):
                c = chr(ord('a') + o)
                t = s + c
                if c in d and t in l:
                    traversal(s + c, d[c])

        traversal('', d)
        return ret[0]


if __name__ == '__main__':
    print(Solution().longestWord(["w", "wo", "wor", "worl", "world"]))
