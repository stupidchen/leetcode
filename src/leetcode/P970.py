class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ret = []
        i, j = 0, 0
        while x ** i <= bound and x > 1:
            i += 1
        while y ** j <= bound and y > 1:
            j += 1

        if x <= 1:
            i = 1
        if y <= 1:
            j = 1

        for ti in range(i):
            for tj in range(j):
                if x ** ti + y ** tj <= bound:
                    ret.append(x ** ti + y ** tj)
                else:
                    break

        return list(set(ret))

if __name__ == '__main__':
    print(Solution().powerfulIntegers(1, 2, 100))
