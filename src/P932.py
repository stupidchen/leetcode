class Solution:
    def solve(self, a):
        if len(a) <= 2:
            return a
        ret = [[], []]
        for i in range(len(a)):
            ret[i & 1].append(a[i])
        return self.solve(ret[0]) + self.solve(ret[1])

    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        return self.solve([i + 1 for i in range(N)])

    def validate(self, a):
        n = len(a)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(i + 1, j):
                    if a[i] + a[j] == a[k] * 2:
                        print('{} {} {}'.format(i, k, j))
                        return False
        return True


if __name__ == '__main__':
    t = Solution().beautifulArray(33)
    print(Solution().validate(t))
