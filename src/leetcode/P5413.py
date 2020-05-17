class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        t = [(len(words[i]), i, words[i]) for i in range(len(words))]
        t = sorted(t)
        t = [k[2].lower() for k in t]
        t[0] = t[0][0].upper() + t[0][1:]

        return ' '.join(t)


if __name__ == '__main__':
    print()
