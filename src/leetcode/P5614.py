class Solution:
    def mostCompetitive(self, nums, k):
        n = len(nums)
        s = []
        for i, v in enumerate(nums):
            while s and s[-1] > v and k - len(s) < n - i:
                s.pop()
            if len(s) < k:
                s.append(v)

        return s


if __name__ == '__main__':
    print(Solution().mostCompetitive([71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2], 3))
    print(Solution().mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))
