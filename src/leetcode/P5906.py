class Solution:
    def countValidWords(self, sentence: str) -> int:
        c = sentence.split()
        r = 0
        for w in c:
            d = w.count('-')
            s = w.count('.') + w.count('!') + w.count(',')
            n = 0
            for ww in w:
                if ww.isdigit():
                    n += 1
            if d > 1 or s > 1 or n > 0:
                continue
            if d == 1:
                try:
                    i = w.index('-')
                except ValueError:
                    continue
                if i == 0 or i == len(w) - 1:
                    continue
                if not (w[i - 1].isalpha() and w[i + 1].isalpha()):
                    continue
            if s == 1:
                if w[len(w) - 1].isalnum():
                    continue
            r += 1
        return r


if __name__ == '__main__':
    print(Solution().countValidWords("!this  1-s b8d!"))
