class Solution:
    def countElements(self, arr):
        d = set(arr)
        r = 0
        for a in arr:
            if a + 1 in d:
                r += 1
        return r


if __name__ == '__main__':
    print(Solution().countElements([1, 1, 2, 2]))
