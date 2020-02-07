class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        min_num = nums[0]
        max_num = nums[0]
        for num in nums:
            min_num = min(num, min_num)
            max_num = max(num, max_num)
        if max_num == min_num:
            return 0
        m = (max_num - min_num) // (n - 1)
        if m == 0:
            m += 1
        k = (max_num - min_num) // m + 1
        buc = []
        for i in range(k):
            buc.append([-1, -1])
        for num in nums:
            t = (num - min_num) // m
            if buc[t][0] == -1:
                buc[t][0] = num
                buc[t][1] = num
                continue
            buc[t][0] = max(buc[t][0], num)
            buc[t][1] = min(buc[t][1], num)

        ret = 0
        last = -1
        for i in range(k):
            if buc[i][1] == -1:
                continue
            if last != -1:
                ret = max(ret, buc[i][1] - last)
            last = buc[i][0]
        return ret


if __name__ == '__main__':
    print(Solution().maximumGap([1, 1, 1, 1, 1, 5, 5, 5, 5, 5]))
