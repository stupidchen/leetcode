from collections import Counter


class Solution:
    def reorderSpaces(self, text: str) -> str:
        c = Counter(text)
        s = c[' ']
        words = text.split()
        r = ''
        t = 0
        if len(words) != 1:
            t = s // (len(words) - 1)
        for i in range(len(words) - 1):
            r += words[i] + ' ' * t
            s -= t
        r += words[-1] + ' ' * s
        return r


if __name__ == '__main__':
    print('a ')
