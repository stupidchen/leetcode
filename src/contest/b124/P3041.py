from collections import Counter
from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        m = nums[-1]
        f = [[0, 0] for i in range(m + 2)]
        for i in range(1, m + 2):
            current_count = counter[i]
            last_count = counter[i - 1]
            f[i][0] = 0 if current_count == 0 else max(f[i - 1][0], f[i - 1][1]) + 1
            f[i][1] = max(max(f[i - 1][0] + 1, f[i - 1][1] + 1) if last_count > 1 else 0,
                          f[i - 1][1] + 1 if last_count > 0 else 0)
        res = max(map(lambda x: max(x[0], x[1]), f))
        return res


if __name__ == '__main__':
    r = Solution().maxSelectedElements([8, 13, 18, 10, 16, 19, 11, 17, 15, 18, 9, 12, 15, 8, 9, 14, 7])
    # r = Solution().maxSelectedElements(nums=[1, 2, 4, 5, 7, 8])
    print(r)
