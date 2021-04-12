class Solution:
    def constructArray(self, n: int, k: int):
        ret = [1]
        b = True
        for i in reversed(range(1, k + 1)):
            if b:
                ret.append(ret[-1] + i)
            else:
                ret.append(ret[-1] - i)
            b = not b
        for i in range(k + 2, n + 1):
            ret.append(i)
        return ret


if __name__ == '__main__':
    print(Solution().constructArray(10, 4))
