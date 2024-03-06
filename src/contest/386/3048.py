from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        m = len(changeIndices)
        n = len(nums)

        l = 0
        r = m - 1
        solution = -1
        while l <= r:
            mid = (l + r) >> 1

            v = [-1] * n
            for i, ci in enumerate(changeIndices[:mid + 1]):
                v[ci - 1] = max(v[ci - 1], i)

            p = []
            solvable = True
            for i, t in enumerate(v):
                if t == -1:
                    solvable = False
                else:
                    p.append((t, i))
            if solvable:
                p = sorted(p)
                c = n - 1
                o = [None] * (p[c][0] + 1)
                for i, t in enumerate(v):
                    o[t] = -1
                while c >= 0:
                    s = p[c][0] - 1
                    j = 0
                    solved = True
                    while j < nums[p[c][1]]:
                        while s >= 0 and o[s] is not None:
                            s -= 1
                        if s < 0:
                            solved = False
                            break
                        o[s] = p[c][1]
                        s -= 1
                        j += 1
                    if not solved:
                        break
                    c -= 1
            else:
                c = 0

            if c >= 0:
                l = mid + 1
            else:
                r = mid - 1
                solution = mid

        if solution != -1:
            solution += 1
        return solution


if __name__ == '__main__':
    r = Solution().earliestSecondToMarkIndices(nums=[7, 7], changeIndices=[1, 2])
    print(r)
