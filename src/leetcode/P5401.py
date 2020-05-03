class Solution:
    def kLengthApart(self, nums, k: int):
        n = len(nums)
        last = None
        for i in range(n):
            if nums[i] == 1:
                if last is not None:
                    if i - last <= k:
                        return False
                last = i
        return True


if __name__ == '__main__':
    print(Solution().kLengthApart(nums = [0, 1, 0, 1], k = 1))
