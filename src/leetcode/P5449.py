from collections import defaultdict


class Solution:
    def canArrange(self, arr, k) -> bool:
        n = len(arr)
        d = defaultdict(lambda: 0)
        for i in range(n):
            arr[i] = arr[i] % k
            d[arr[i]] += 1

        for i in range(1, k):
            if d[k - i] != d[i] or (k - i == i and (d[k - i] & 1 == 1)):
                return False
        return True

