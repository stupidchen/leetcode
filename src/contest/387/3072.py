import bisect
from typing import List

from sortedcontainers import SortedList

def greaterCount(arr, val):
    return len(arr) - bisect.bisect_right(arr, val)


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1, a2 = [nums[0]], [nums[1]]
        sa1, sa2 = SortedList(a1), SortedList(a2)
        for num in nums[2:]:
            c1, c2 = greaterCount(sa1, num), greaterCount(sa2, num)
            if c1 > c2:
                a1.append(num)
                sa1.add(num)
            elif c1 < c2:
                a2.append(num)
                sa2.add(num)
            elif len(a1) <= len(a2):
                a1.append(num)
                sa1.add(num)
            else:
                a2.append(num)
                sa2.add(num)
        return a1 + a2
