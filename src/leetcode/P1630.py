from collections import Counter


class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        ret = []
        m = len(l)
        for q in range(m):
            ql, qr = l[q], r[q]
            min_num = min(nums[ql:qr + 1])
            max_num = max(nums[ql:qr + 1])
            t = qr - ql + 1
            d = (max_num - min_num) // (t - 1)

            s = Counter(nums[ql:qr + 1])
            can = True
            for i in range(t):
                k = min_num + i * d
                if k not in s or s[k] <= 0:
                    can = False
                    break
                s[k] -= 1
            ret.append(can)
        return ret


if __name__ == '__main__':
    print(Solution().checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[2, 0, 0], r=[5, 2, 3]))
