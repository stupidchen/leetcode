class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        s = [i for i in range(27)]

        def find(i):
            if s[i] != i:
                s[i] = find(s[i])
            return s[i]

        def merge(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                s[rx] = ry

        for e in equations:
            op1, op2 = ord(e[0]) - ord('a'), ord(e[3]) - ord('a')
            if e[1:3] == '==':
                merge(op1, op2)

        for e in equations:
            op1, op2 = ord(e[0]) - ord('a'), ord(e[3]) - ord('a')
            if e[1:3] == '!=':
                if find(op1) == find(op2):
                    return False
        return True


if __name__ == '__main__':
    print(Solution().equationsPossible(["c==c","b==d","x!=z"]))
