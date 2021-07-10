class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        lq, rq = 0, 0
        s = 0
        for i in range(n):
            if num[i] == '?':
                if i < n >> 1:
                    lq += 1
                else:
                    rq += 1
            else:
                if i < n >> 1:
                    s += int(num[i])
                else:
                    s -= int(num[i])
        q = (lq + rq) >> 1
        if s == 0:
            return lq != rq
        elif s > 0:
            return lq >= rq or (s + (lq - q) * 9 != 0)
        else:
            return lq <= rq or (s - (rq - q) * 9 != 0)


if __name__ == '__main__':
    print(Solution().sumGame("112?"))
    print(Solution().sumGame("?3295???"))
