class Solution:
    def processQueries(self, queries, m):
        r = []
        a = [i + 1 for i in range(m)]
        for q in queries:
            t = a.index(q)
            r.append(t)
            a = [a[t]] + a[:t] + a[t + 1:]
        return r

if __name__ == '__main__':
    print(Solution().processQueries(queries = [7,5,5,8,3], m = 8))
