class Solution:
    def removeDuplicates(self, nums):
        l = 0
        t = None
        c = 0
        for i, v in enumerate(nums):
            if t != v:
                t = v
                c = 1
                nums[l] = v
                l += 1
            else:
                if c == 2:
                    continue
                else:
                    c += 1
                    nums[l] = v
                    l += 1

        return l


if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
