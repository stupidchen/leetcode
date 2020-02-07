class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        n = len(stations)
        if n == 0:
            if startFuel >= target:
                return 0
            return -1
        f = []
        for i in range(n + 1):
            f.append([-1] * (n + 1))
        t = [-1] * (n + 1)
        stations.insert(0, [0, startFuel])
        f[0][0] = startFuel
        t[0] = 0
        ans = -1
        n += 1
        for i in range(1, n):
            d = target - stations[i][0]
            l = i + 1
            if ans != -1:
                l = min(ans, l)
            for j in range(l):
                if t[j] != -1:
                    s = stations[i][0] - stations[t[j]][0]
                    if f[t[j]][j] >= s:
                        f[i][j] = f[t[j]][j] - s
                if j > 0 and t[j - 1] != -1:
                    ll = f[t[j - 1]][j - 1]
                    s = stations[i][0] - stations[t[j - 1]][0]
                    if ll >= s:
                        f[i][j] = max(f[i][j], ll - s + stations[i][1])
            for j in range(l):
                if f[i][j] != -1:
                    if t[j] == -1 or f[t[j]][j] + stations[t[j]][0] <= f[i][j] + stations[i][0]:
                        t[j] = i
                    if d <= f[i][j]:
                        if ans == -1 or ans > j:
                            ans = j
                            break
        return ans


if __name__ == '__main__':
    print(Solution().minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))
