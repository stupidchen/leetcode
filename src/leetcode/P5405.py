class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        f = [[0] * n for i in range(n)]
        for i in range(n):
            f[i][i] = arr[i]
            for j in range(i + 1, n):
                f[i][j] = f[i][j - 1] ^ arr[j]

        r = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(i, j):
                    if f[i][k] == f[k + 1][j]:
                        r += 1
        return r


if __name__ == '__main__':
    print(Solution().countTriplets([2, 3]))
    print(Solution().countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]))
