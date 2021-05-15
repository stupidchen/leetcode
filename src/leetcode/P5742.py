class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        r = [''] * len(words)
        for word in words:
            tword = word[:-1]
            i = int(word[-1])
            r[i - 1] = tword
        return ' '.join(r)


if __name__ == '__main__':
    print(Solution().sortSentence("Myself2 Me1 I4 and3"))
