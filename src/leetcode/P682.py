from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for e in ops:
            if e == 'C':
                s.pop()
            elif e == 'D':
                s.append(s[-1] << 1)
            elif e == '+':
                s.append(s[-2] + s[-1])
            else:
                s.append(int(e))

        return sum(s)
