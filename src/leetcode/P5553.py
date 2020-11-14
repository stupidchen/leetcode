from collections import Counter


class Solution:
    def canDistribute(self, nums, quantity) -> bool:
        quantity = sorted(quantity, reverse=True)
        nums = sorted(list(Counter(nums).values()), reverse=True)
        n = len(quantity)
        m = len(nums)

        ret = [False]

        def find(x):
            if x == n:
                ret[0] = True
                return

            q = quantity[x]
            t = max(nums)
            if t < q:
                return

            for i in range(m):
                if nums[i] >= q:
                    nums[i] -= q
                    find(x + 1)
                    if ret[0]:
                        return
                    nums[i] += q

        find(0)
        return ret[0]


if __name__ == '__main__':
    print(Solution().canDistribute([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,30,31,31,32,32,33,33,34,34,35,35,36,36,37,37,38,38,39,39], [2,2,2,2,2,2,2,2,2,2]))
    print(Solution().canDistribute([1, 2, 3, 4], [2]))
    print(Solution().canDistribute([1, 1, 2, 2], [2, 3]))
