import copy


class Solution:
    ret = []

    ans = []

    def solve(self, k0, k1, n, ans):
        if k0 >= k1:
            if n == 0:
                self.ret.append(copy.deepcopy(ans))
            return

        if k0 > 0:
            start = ans[k0 - 1] + 1
        else:
            start = 1

        for i in range(start, n + 1):
            if i <= 9:
                ans[k0] = i
                self.solve(k0 + 1, k1, n - i, ans)
            else:
                break

    def combinationSum3(self, k, n):
        self.ret = []
        self.solve(0, k, n, [0] * k)
        return self.ret

if __name__ == '__main__':
    print(Solution().combinationSum3(2, 18))
