from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1, n2 = len(nums1), len(nums2)

        def s(a, l):
            r = []
            for i, v in enumerate(a):
                while r and v > r[-1] and len(a) - i + len(r) > l:
                    r.pop()
                r.append(v)
            return r[:l]

        ret = []
        for i in range(k + 1):
            if i <= n1 and k - i <= n2:
                s1 = s(nums1, i)
                s2 = s(nums2, k - i)
                c = []
                p1 = p2 = 0
                while (p1 < len(s1)) and (p2 < len(s2)):
                    if s1[p1:] < s2[p2:]:
                        c.append(s2[p2])
                        p2 += 1
                    else:
                        c.append(s1[p1])
                        p1 += 1
                c.extend(s1[p1:])
                c.extend(s2[p2:])
                ret = max(ret, c)

        return ret


if __name__ == '__main__':
    print(Solution().maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15))
