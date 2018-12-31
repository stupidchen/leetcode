VOWELS = 'AEIOU'


class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        n, m = len(wordlist), len(queries)
        iwordlist = [w.upper() for w in wordlist]
        vqd, iqd, qd = {}, {}, {}

        def mark(origin, word, n, i):
            if i == n:
                nword = ''.join(word)
                if nword not in vqd:
                    vqd[nword] = origin
                return

            if word[i] in VOWELS:
                for v in VOWELS:
                    word[i] = v
                    mark(origin, word, n, i + 1)
            else:
                mark(origin, word, n, i + 1)

        for i in range(n):
            if iwordlist[i] not in iqd:
                iqd[iwordlist[i]] = wordlist[i]
            qd[wordlist[i]] = wordlist[i]
            mark(wordlist[i], list(iwordlist[i]), len(iwordlist[i]), 0)


        ret = []
        for i in range(m):
            if queries[i] in qd:
                ret.append(queries[i])
                continue

            uq = queries[i].upper()
            if uq in iqd:
                ret.append(iqd[uq])
                continue

            if uq in vqd:
                ret.append(vqd[uq])
                continue

            ret.append('')

        return ret


if __name__ == '__main__':
    print(Solution().spellchecker(["KiTe", "kite", "hare", "Hare"],
                                  ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]))
