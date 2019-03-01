class Solution:
    def wiggleMaxLength(self, nums):
        n = len(nums)
        if n <= 2:
            return n

        inc = None
        t = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] and inc is None:
                continue
            else:
                if nums[i] < nums[i - 1]:
                    inc = True
                else:
                    inc = False


            if (inc and nums[i] > nums[i - 1]) or (not inc and nums[i] < nums[i - 1]) :
                t += 1
                inc = not inc

        return t

if __name__ == '__main__':
    print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))