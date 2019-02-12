class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        ret = 0
        n = len(A)
        i = 0
        while i < n - 2:
            d = A[i + 1] - A[i]
            j = i + 1
            while j < n - 1:
                if A[j + 1] - A[j] != d:
                    break
                j += 1
            l = j - i
            ret += (l * (l - 1)) >> 1
            i = j
        return ret


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))
