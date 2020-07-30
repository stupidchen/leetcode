class Solution:
    def closestToTarget(self, arr, target):
        n = len(arr)
        m = 20
        b = [[0] * (n + 1) for i in range(20)]
        for i in range(n):
            for j in range(m):
                b[j][i + 1] = b[j][i]
                if arr[i] | (1 << j) == arr[i]:
                    b[j][i + 1] += 1

        def func(l, r):
            ret = 0
            t = r - l + 1
            for j in range(m):
                if b[j][r + 1] - b[j][l] == t:
                    ret += 1 << j
            return ret

        ret = None
        l, r = 0, 0

        while l < n and r < n:
            t = func(l, r)
            if ret is None or ret > abs(t - target):
                ret = abs(t - target)
            if t == target:
                break
            if t < target:
                l += 1
                if l > r:
                    r = l
            else:
                r += 1

        return ret


if __name__ == '__main__':
    print(Solution().closestToTarget([1, 2, 4, 8, 16], 3))
    print(Solution().closestToTarget([10102] * 10 ** 5, 22))
    print(Solution().closestToTarget([5, 89, 79, 44, 45, 79], 965))
