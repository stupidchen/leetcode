from collections import defaultdict
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        kv = sorted(zip(values, labels), reverse=True)
        ret = 0
        d = defaultdict(lambda: useLimit)
        p = -1
        for i in range(numWanted):
            while True:
                p += 1
                if p == len(kv) or d[kv[p][1]] > 0:
                    break
            if p == len(kv):
                break
            value, label = kv[p]
            ret += value
            d[label] -= 1
        return ret


if __name__ == '__main__':
    print(Solution().largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], numWanted=3, useLimit=1))
