VOWELS = 'aeiouAEIOU'


class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()

        for i in range(len(words)):
            f = words[i][0]
            if f in VOWELS:
                words[i] += 'ma'
            else:
                words[i] = words[i][1:] + f + 'ma'

            words[i] += 'a' * (i + 1)
        return ' '.join(words)
