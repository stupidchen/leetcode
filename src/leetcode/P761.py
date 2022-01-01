class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def dfs(x):
            ret = []
            t = 0
            last = 0
            for i, c in enumerate(x):
                t += 1 if c == '1' else -1
                if t == 0:
                    ret.append('1' + dfs(x[last + 1:i]) + '0')
                    last = i + 1
            ret.sort(reverse=True)
            return ''.join(ret)

        return dfs(s)


if __name__ == '__main__':
    print(Solution().makeLargestSpecial('01'))
