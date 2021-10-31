from typing import List

MIN = 0
MAX = 1000


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = [start]

        r = set()
        for i in range(MIN, MAX + 1):
            for num in nums:
                if i + num == goal or i - num == goal or i ^ num == goal:
                    r.add(i)

        h = 0
        if start in r:
            return 1
        s = {start: 0}
        while h < len(q):
            c = q[h]
            f = s[c]
            for num in nums:
                t = c + num
                if MIN <= t <= MAX and t not in s:
                    s[t] = f + 1
                    if t in r:
                        return s[t] + 1
                    q.append(t)

                t = c - num
                if MIN <= t <= MAX and t not in s:
                    s[t] = f + 1
                    if t in r:
                        return s[t] + 1
                    q.append(t)

                t = c ^ num
                if MIN <= t <= MAX and t not in s:
                    s[t] = f + 1
                    if t in r:
                        return s[t] + 1
                    q.append(t)
            h += 1

        return -1


if __name__ == '__main__':
    print(Solution().minimumOperations(nums=[2, 8, 16], start=0, goal=1))
