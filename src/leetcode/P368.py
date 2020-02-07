class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        nums = sorted(nums)
        f, t = [1] * n, [-1] * n
        max_set, target = 0, 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and f[j] + 1 > f[i]:
                    f[i] = f[j] + 1
                    t[i] = j
            if f[i] > max_set:
                max_set, target = f[i], i

        ret = []
        while target != -1:
            ret.append(nums[target])
            target = t[target]
        return ret


if __name__ == '__main__':
    print(Solution().largestDivisibleSubset([1]))
