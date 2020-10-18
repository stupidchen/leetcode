class Solution:
    def bestTeamScore(self, scores, ages):
        n = len(scores)
        a = []
        for i in range(n):
            a.append((scores[i], ages[i]))
        a = sorted(a)
        f = [0] * n
        r = 0
        for i in range(n):
            f[i] = a[i][0]
            for j in range(i):
                if a[i][1] >= a[j][1]:
                    f[i] = max(f[j] + a[i][0], f[i])
            r = max(r, f[i])
        return r


if __name__ == '__main__':
    print(Solution().bestTeamScore([1, 3, 7, 3, 2, 4, 10, 7, 5], [4, 5, 2, 1, 1, 2, 4, 1, 4]))
