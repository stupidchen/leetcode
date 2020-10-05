class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        return ((1 << N.bit_length()) - 1) - N


if __name__ == '__main__':
    print(Solution().bitwiseComplement(5))
