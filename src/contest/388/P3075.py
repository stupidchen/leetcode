from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(key=lambda x: -x)
        res = 0
        for i in range(k):
            res += max(happiness[i] - i, 0)
        return res


if __name__ == '__main__':
    r = Solution().maximumHappinessSum(happiness=[1, 2, 3], k=2)
    print(r)
