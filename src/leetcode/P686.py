class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = (len(b) - 1) // len(a) + 1
        t = a * n
        for i in range(n + 1):
            if t.find(b) >= 0:
                return n + i
            t += a
        return -1


if __name__ == '__main__':
    print(Solution().repeatedStringMatch(a="a", b="aa"))
