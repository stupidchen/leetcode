class Solution:
    def peopleIndexes(self, favoriteCompanies):
        n = len(favoriteCompanies)
        f = [set(c) for c in favoriteCompanies]
        r = []
        for i in range(n):
            t = True
            for j in range(n):
                if i != j and len(f[i]) <= len(f[j]):
                    if f[i] & f[j] == f[i]:
                        t = False
                        break
            if t:
                r.append(i)
        return r


if __name__ == '__main__':
    print(Solution().peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]))
