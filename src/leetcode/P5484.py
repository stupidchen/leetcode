class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'

        for i in range(n - 1):
            s = s + '1' + ''.join(reversed([chr(97 - ord(c)) for c in s]))
        return s[k - 1]


if __name__ == '__main__':
    print(Solution().findKthBit(20, 1))
