class Solution(object):
    def uncommonFromSentences(self, A, B):
        a = {}
        b = {}
        for word in B.split(' '):
            b[word] = b.setdefault(word, 0) + 1
        for word in A.split(' '):
            a[word] = a.setdefault(word, 0) + 1
        ret = []
        for word in a.keys():
            if word not in b and a[word] == 1:
                ret.append(word)
        for word in b.keys():
            if word not in a and b[word] == 1:
                ret.append(word)
        return ret

if __name__ == '__main__':
    print(Solution().uncommonFromSentences("this apple is sweet","this apple is sour"))