class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        r = 0
        k = n.bit_length()
        t = 0
        for i in reversed(range(k)):
            t += 1 << i
            if (m >= t and n >= t) or (m < t and n < t):
                if m < t:
                    t -= 1 << i
            else:
                t -= 1 << i
                break
        return t


if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(4, 5))
