class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k -= 1
        r = 0
        for i in reversed(range(n)):
            if k >= (1 << i):
                r = 1 - r
                k -= 1 << i
        return r


if __name__ == '__main__':
    print(Solution().kthGrammar(3, 8))
