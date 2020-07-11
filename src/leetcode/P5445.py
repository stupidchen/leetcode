class Solution:
    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        f = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + nums[i]
        s = []
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                s.append(f[j] - f[i])
        s = sorted(s)
        return sum(s[left - 1: right])


if __name__ == '__main__':
    print(Solution().rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))
