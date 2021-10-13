from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        t = set(list1) & set(list2)
        r = [(list1.index(tt) + list2.index(tt), tt) for tt in t]
        r.sort()
        return list(map(lambda p: p[1], filter(lambda p: p[0] == r[0][0], r)))

