from collections import Counter
from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        c1, c2 = Counter(nums1), Counter(nums2)
        res = 0
        count1 = h1 = len(nums1) >> 1
        count2 = h2 = len(nums2) >> 1
        d1 = s1 - s2
        for k in d1:
            count1 -= min(c1[k] - 1, count1)

        d2 = s2 - s1
        for k in d2:
            count2 -= min(c2[k] - 1, count2)

        count1 -= max(0, len(d1) - h1)
        count2 -= max(0, len(d2) - h2)
        res += min(len(d1), h1)
        res += min(len(d2), h2)

        intersection = s1 & s2
        m = len(intersection)
        m1 = m2 = 0
        for k in intersection:
            m1 += c1[k] - 1
            m2 += c2[k] - 1

        if count1 <= m1 or count2 <= m2:
            res += m
            return res

        count1 -= m1
        count2 -= m2
        res += m - max(count1 + count2 - m, 0)
        return res


if __name__ == '__main__':
    r = Solution().maximumSetSize(nums1=[1, 1, 2, 2, 3, 3], nums2=[4, 4, 5, 5, 6, 6])
    print(r)
