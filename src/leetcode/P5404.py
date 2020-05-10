class Solution:
    def buildArray(self, target, n):
        m = len(target)
        c = 0
        r = []
        s = []
        for i in range(n):
            t = i + 1
            if c >= m:
                break
            r.append('Push')
            if t != target[c]:
                r.append('Pop')
            else:
                c += 1
                s.append(t)

        return r


if __name__ == '__main__':
    print(Solution().buildArray(target = [2,3,4], n = 4))
