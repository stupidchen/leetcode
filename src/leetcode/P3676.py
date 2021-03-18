class Solution:
    def wiggleMaxLength(self, nums):
        n = len(nums)
        if n < 2:
            return n

        inc = None
        t = 1
        for i in range(1, n):
            if inc is None:
                if nums[i] == nums[i - 1]:
                    continue
                else:
                    if nums[i] < nums[i - 1]:
                        inc = True
                    else:
                        inc = False

            if (inc and nums[i] < nums[i - 1]) or (not inc and nums[i] > nums[i - 1]):
                t += 1
                inc = not inc

        return t
