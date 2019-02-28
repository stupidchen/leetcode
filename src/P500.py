class Solution:
    def findWords(self, words):
        rows = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        d = {}
        for i in range(len(rows)):
            for j in rows[i]:
                d[j] = i
        ret = []
        for word in words:
            if len(word) == 0:
                ret.append(word)
            t = d[word[0].upper()]
            c = True
            for l in word:
                if d[l.upper()] != t:
                    c = False
                    break
            if c:
                ret.append(word)
        return ret
