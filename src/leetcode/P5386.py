from collections import Counter


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def canBreak(x, y):
            cx, cy = dict(Counter(x)), dict(Counter(y))
            for i in range(26):
                c = chr(97 + i)
                if c not in cx:
                    cx[c] = 0
                if c not in cy:
                    cy[c] = 0

            tx, ty = 0, 0
            for i in range(26):
                c = chr(97 + i)
                tx += cx[c]
                ty += cy[c]
                if tx < ty:
                    return False
            return True

        return canBreak(s1, s2) or canBreak(s2, s1)


if __name__ == '__main__':
    print(Solution().checkIfCanBreak('ed', 'ib'))
