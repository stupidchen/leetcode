class Solution:
    def consecutiveNumbersSum(self, N):
        n = 2 * N
        ans = 0 
        for i in range(1, n):
            if i * i >= n:
                break
            if n % i == 0:
                if (int(n / i) - i) & 1 != 0:
                    ans += 1
        return ans
