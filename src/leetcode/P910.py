class Solution:
    def smallestRangeII(self, A, K):
        tmp = max(A) - min(A)
        n = len(A)
        B = sorted(A)
        t = 0xffffffff
        min_num = B[0] + K
        max_num = B[n - 1] - K
        for i in range(n - 1):
            tmax = B[i] + K
            tmin = B[i + 1] - K
            t = min(t, max(max_num, tmax) - min(min_num, tmin))
        return min(tmp, t)



if __name__ == '__main__':
    print(Solution().smallestRangeII([7 ,8 ,8, 1, 5, 2], 4))
