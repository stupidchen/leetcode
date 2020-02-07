class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        t = [A, B]

        ret = ''
        count = [0, 0]
        for i in range(A + B):
            if t[0] > t[1]:
                if count[0] < 2 and t[0] > 0:
                    c = 0
                else:
                    c = 1
            else:
                if count[1] < 2 and t[1] > 0:
                    c = 1
                else:
                    c = 0

            if c == 0:
                ret += 'a'
                t[0] -= 1
            else:
                ret += 'b'
                t[1] -= 1

            s = ret[max(0, len(ret) - 2):]
            count = [0, 0]
            for ss in s:
                if ss == 'a':
                    count[0] += 1
                else:
                    count[1] += 1

        return ret


if __name__ == '__main__':
    print(Solution().strWithout3a3b(8,8))
