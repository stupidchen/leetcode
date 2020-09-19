class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        n = len(arr)
        f = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + arr[i]

        r = 0
        for i in range(((n - 1) >> 1) + 1):
            t = ((i + 1) << 1) - 1
            for j in range(n - t + 1):
                r += f[j + t] - f[j]
        return r


if __name__ == '__main__':
    print(Solution().sumOddLengthSubarrays([1]))
