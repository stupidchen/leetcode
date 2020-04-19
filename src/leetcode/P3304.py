import bisect


class Solution:
    def search(self, nums, target):
        def _search(l, r):
            if l >= r:
                return -1
            if nums[l] <= nums[r - 1]:
                t = bisect.bisect_left(nums, target, l, r)
                if t < r and nums[t] == target:
                    return t
                else:
                    return -1
            else:
                mid = (l + r) >> 1
                tl, tr = _search(l, mid), _search(mid, r)
                if tl == -1:
                    return tr
                else:
                    return tl

        return _search(0, len(nums))


if __name__ == '__main__':
    print(Solution().search([], 5))
