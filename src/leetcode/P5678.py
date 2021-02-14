class Solution:
    def minimumSize(self, nums, maxOperations):
        nums = sorted(nums, reverse=True)
        n = len(nums)

        def can(b):
            rr = 0
            for i in range(n):
                rr += (nums[i] - 1) // b
                if rr > maxOperations:
                    return False
                if nums[i] <= b:
                    break

            return True

        l, r = 1, max(nums)
        ret = None
        while l <= r:
            mid = (l + r) >> 1
            if can(mid):
                ret = mid
                r = mid - 1
            else:
                l = mid + 1

        return ret


if __name__ == '__main__':
    print(Solution().minimumSize(nums=[7, 17], maxOperations=2))
