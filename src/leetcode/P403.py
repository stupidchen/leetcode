from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        f = {(0, 0): 0}
        q = [(0, 0)]
        h = 0
        while h < len(q):
            last, step = q[h]
            count = f[q[h]]
            stone = stones[last]
            for i in range(last + 1, n):
                k = stones[i] - stone
                if abs(k - step) <= 1:
                    if (i, k) not in f:
                        if i == n - 1:
                            return True
                        f[(i, k)] = count + 1
                        q.append((i, k))
                elif k - step > 1:
                    break
            h += 1
        return False


if __name__ == '__main__':
    print(Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17]))
