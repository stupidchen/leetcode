class Solution:
    def selfDividingNumbers(self, left, right):
        ret = []

        def judge(x):
            t = x
            while t > 0:
                k = t % 10
                if k == 0 or x % k != 0:
                    return False
                t //= 10
            return True

        for i in range(left, right + 1):
            if judge(i):
                ret.append(i)
        return ret


if __name__ == '__main__':
    print(Solution().selfDividingNumbers(1, 10))
