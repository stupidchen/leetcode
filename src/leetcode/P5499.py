class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m + 1):
            t = 1
            j = i + m
            while j < n:
                if arr[i: i + m] == arr[j: j + m]:
                    t += 1
                else:
                    break
                j += m
            if t >= k:
                return True
        return False


if __name__ == '__main__':
    print(Solution().containsPattern([1, 2, 3, 1, 2], 2, 2))
