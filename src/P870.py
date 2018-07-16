class Solution:
    def advantageCount(self, A, B):
        n = len(A)
        a = sorted(A)
        tb = []
        for i in range(n):
            tb.append((i, B[i]))
        tb = sorted(tb, key=lambda b: b[1])
        j = 0
        ret = [None] * n
        if n == 0:
            return ret
        s = [False] * n
        for i in range(n):
            while j < n and a[j] <= tb[i][1]:
                j += 1
            if j < n:
                ret[tb[i][0]] = a[j]
                s[j] = True
            else:
                j = 0
                for k in range(n):
                    if not s[k]:
                        while j < n and ret[j] is not None:
                            j += 1
                        ret[j] = a[k]
                return ret
            j += 1
        return ret


if __name__ == '__main__':
    print(Solution().advantageCount([2, 1], [3, 4]))
