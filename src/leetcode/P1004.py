class Solution:
    def longestOnes(self, A, K: int) -> int:
        i = 0
        n = len(A)
        a = []
        while i < n:
            t = A[i]
            j = i + 1
            while j < n and A[j] == t:
                j += 1
            if t == 1:
                a.append(j - i)
            else:
                a.append(-(j - i))
            i = j

        m = max(a)
        if m < 0:
            ret = K
        else:
            ret = max(a) + K
        t, k = 0, K
        l = 0
        for i in range(len(a)):
            if a[i] > 0:
                t += a[i]
            else:
                while k + a[i] < 0 and l < i:
                    if a[l] > 0:
                        t -= a[l]
                    else:
                        t += a[l]
                        k -= a[l]
                    l += 1
                if k + a[i] >= 0 and a[l] > 0:
                    t -= a[i]
                    k += a[i]
                else:
                    l = i + 1
                    k = K
            if l < i and min(t + k, n) > ret:
                ret = min(t + k, n)
                # print('{}~{}:{}'.format(l, i, ret))
        return ret

if __name__ == '__main__':
    print(Solution().longestOnes([1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], 8))
