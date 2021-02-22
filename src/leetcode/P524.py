class Solution:
    def findLongestWord(self, s, d):
        def can(x, y):
            t = 0
            n = len(x)
            for c in y:
                found = False
                while t < n:
                    if x[t] == c:
                        found = True
                        break
                    t += 1
                if not found:
                    return False
                t += 1
            return True

        ret = ''
        for ds in d:
            if can(s, ds):
                if len(ret) < len(ds) or (len(ret) == len(ds) and ret > ds):
                    ret = ds
        return ret
