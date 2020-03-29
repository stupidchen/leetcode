from collections import Counter


class Solution:
    def findLucky(self, arr):
        d = Counter(arr)
        r = -1
        for k, v in d.items():
            if k == v:
                r = max(r, k)
        return r


if __name__ == '__main__':
    print(Solution().findLucky([2, 2, 3, 4]))
    print(Solution().findLucky([1, 2, 2, 3, 3, 3]))
