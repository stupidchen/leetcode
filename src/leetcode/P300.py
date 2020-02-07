class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {0: -0xffffffff}
        for num in nums:
            l = 0
            r = len(d) - 1
            tmp = None
            while l <= r:
                mid = (l + r) >> 1
                if d[mid] < num:
                    tmp = mid
                    l = mid + 1
                else:
                    r = mid - 1
            if tmp is not None:
                d[tmp + 1] = min(num, d.setdefault(tmp + 1, 0xffffffff))
            else:
                d[1] = min(d[1], num)
        return max(d.keys())


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10, 11]))
