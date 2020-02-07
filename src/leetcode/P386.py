class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []

        def solve(d):
            if d <= n:
                ret.append(d)

            for i in range(10):
                t = d * 10 + i
                if t <= n:
                    solve(t)
                else:
                    break

        for i in range(1, 10):
            solve(i)
        return ret


if __name__ == '__main__':
    print(Solution().lexicalOrder(13))
