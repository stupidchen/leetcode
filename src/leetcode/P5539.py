from collections import Counter


class Solution:
    def frequencySort(self, nums):
        d = Counter(nums)
        t = [(d[i], -i) for i in d.keys()]
        t = sorted(t)
        r = []
        for time, num in t:
            r += [-num] * time
        return r

if __name__ == '__main__':
    print(Solution().frequencySort([1, 1, 2, 2, 2, 3]))
