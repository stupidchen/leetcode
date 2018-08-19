class Solution:
    def compile(self, p):
        l = len(p)
        v = [False] * l
        ret = {}
        for i in range(l):
            if not v[i]:
                v[i] = True
                ret.setdefault(i, []).append(i)
                for j in range(l):
                   if not v[j] and p[i] == p[j]:
                       v[j] = True
                       ret[i].append(j)
        return ret

    def findAndReplacePattern(self, words, pattern):
        p = self.compile(pattern)
        ret = []
        l = len(pattern)
        for word in words:
            if len(word) != l:
                continue
            tmp = ['*'] * l
            can = True
            use = {}
            for i in range(l):
                if tmp[i] != '*':
                    if tmp[i] != word[i]:
                        can = False
                        break
                    continue
                tmp[i] = word[i]
                if word[i] in use:
                    can = False
                    break
                use[word[i]] = True
                for j in p[i]:
                    if i != j and tmp[j] != '*':
                        can = False
                        break
                    tmp[j] = tmp[i]
                if not can:
                    break
            if can:
                ret.append(word)
        return ret

if __name__ == '__main__':
    print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], 'abb'))