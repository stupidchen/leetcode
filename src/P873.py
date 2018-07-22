class Solution:
    def lenLongestFibSubseq(self, A):
        n = len(A)
        ret = 0
        next = {}
        for i in range(n):
            next[A[i]] = i
        for i in range(n):
            for j in range(i + 1, n):
                l = 0
                l1 = i
                l2 = j
                while A[l1] + A[l2] in next:
                    l += 1
                    t = next[A[l1] + A[l2]]
                    l1 = l2
                    l2 = t
                if l > 0:
                    ret = max(ret, l + 2)
        return ret


if __name__ == '__main__':
    print(Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8,9,10,11,13]))
