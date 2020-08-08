class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        i = 0
        while i < n:
            if s[i] == '(':
                l += 1
                i += 1
                continue
            else:
                rr = 0
                while i < n and s[i] == ')':
                    i += 1
                    rr += 1

                if l << 1 > rr:
                    r += rr & 1
                    l -= (rr + 1) >> 1
                else:
                    r += (((rr + 1) >> 1) - l) + (rr & 1)
                    l = 0
        if l != 0:
            r += l << 1

        return r


if __name__ == '__main__':
    print(Solution().minInsertions("())"))
    print(Solution().minInsertions(s="(("))
    print(Solution().minInsertions(s = "))())("))
    print(Solution().minInsertions(s="(()))"))
