class Solution:
    def getFolderNames(self, names):
        d = {}
        r = []
        for name in names:
            t = name
            s = 0
            if name not in d:
                r.append(name)
            else:
                s = d[name] + 1
                while '{}({})'.format(name, s) in d:
                    s += 1
                t = '{}({})'.format(name, s)
                r.append(t)
            d[name] = s
            d[t] = 0
        return r


if __name__ == '__main__':
    print(Solution().getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]))
