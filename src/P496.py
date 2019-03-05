from collections import defaultdict


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        d = defaultdict(lambda: -1)
        n = len(nums2)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums2[i] < nums2[j]:
                    d[nums2[i]] = nums2[j]
                    break

        ret = []
        for num in nums1:
            ret.append(d[num])
        return ret
