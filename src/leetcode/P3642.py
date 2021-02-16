class Solution:
    def letterCasePermutation(self, S):
        letters = []
        for i, c in enumerate(S):
            if c.isalpha():
                letters.append(i)

        r = []
        n = len(letters)
        for i in range(1 << n):
            t = list(S)
            for j in range(n):
                if i | (1 << j) == i:
                    t[letters[j]] = t[letters[j]].lower()
                else:
                    t[letters[j]] = t[letters[j]].upper()
            r.append(''.join(t))
        return r
