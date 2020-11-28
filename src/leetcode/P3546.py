class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        p = [(nums[i], i) for i in range(n)]
        p = list(reversed(sorted(p, key=lambda t: t[0])))
        ret = [None] * (n - k + 1)
        m = 0
        for i in range(n):
            for j in range(max(0, p[i][1] - k + 1), min(p[i][1] + 1, n - k + 1)):
                if ret[j] is None:
                    ret[j] = p[i][0]
                    m += 1
            if m == n - k + 1:
                break
        return ret


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
