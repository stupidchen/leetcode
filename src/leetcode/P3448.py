from collections import Counter


class Solution:
    def partitionLabels(self, S):
        c = Counter(S)
        r = []
        p = set()
        l = -1
        for i in range(len(S)):
            p.add(S[i])
            c[S[i]] -= 1
            ok = True
            for ch in p:
                if c[ch] != 0:
                    ok = False
                    break
            if ok:
                r.append(i - l)
                l = i
                p = set()
        return r


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
