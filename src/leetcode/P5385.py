class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        maxn = num
        for i in range(10):
            maxn = max(maxn, int(s.replace(str(i), '9')))

        minn = num
        for i in range(10):
            for j in range(2):
                t = s.replace(str(i), str(j))
                if t[0] != '0':
                    minn = min(minn, int(t))
        return maxn - minn


if __name__ == '__main__':
    print(Solution().maxDiff(1))
