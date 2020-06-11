from collections import Counter


class Solution:
    def canBeEqual(self, target, arr):
        return Counter(target) == Counter(arr)
