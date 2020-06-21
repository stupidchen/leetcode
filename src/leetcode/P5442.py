class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        r = [-1] * n
        t = {}
        d = set()
        for i in range(n):
            rain = rains[i]
            if rain > 0:
                if rain in t:
                    found = None
                    for j in d:
                        if t[rain] < j < i:
                            found = j
                            break
                    if found is not None:
                        r[found] = rain
                        d.remove(found)
                    else:
                        return []
                t[rain] = i
            else:
                d.add(i)

        for i in range(n):
            rain = rains[i]
            if rain == 0 and r[i] == -1:
                r[i] = 1

        return r


if __name__ == '__main__':
    print(Solution().avoidFlood([2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2]))
