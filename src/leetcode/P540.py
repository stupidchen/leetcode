class Solution:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1

            if mid > 0 and nums[mid] == nums[mid - 1]:
                if mid & 1 == 0:
                    r = mid - 2
                else:
                    l = mid + 1
                continue

            if mid < r and nums[mid] == nums[mid + 1]:
                if mid & 1 == 1:
                    r = mid - 1
                else:
                    l = mid + 2
                continue

            return nums[mid]

        return nums[l]


if __name__ == '__main__':
    print(Solution().singleNonDuplicate([1, 1, 2, 3, 3]))
