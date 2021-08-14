from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes):
        @lru_cache(maxsize=None)
        def f(l, r, k):
            if l > r:
                return 0
            while l + 1 <= r and boxes[l] == boxes[l + 1]:
                k += 1
                l += 1
            ret = f(l + 1, r, 0) + (k + 1) ** 2
            for j in range(l + 1, r + 1):
                if boxes[l] == boxes[j]:
                    ret = max(ret, f(j, r, k + 1) + f(l + 1, j - 1, 0))
            return ret

        return f(0, len(boxes) - 1, 0)


if __name__ == '__main__':
    print(Solution().removeBoxes([1, 2]))
    print(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))
    print(Solution().removeBoxes([1, 1, 1]))
