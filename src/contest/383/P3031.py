BASE = 11
MODULO = 10 ** 20 + 9
ALPHABET_START = ord('a') - 1


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        m = n % k
        hit = set()
        fh = 0
        if m != 0:
            for i in range(m):
                fh = (fh * BASE + (ord(word[i]) - ALPHABET_START)) % MODULO
            hit.add(fh)

        for i in range(n // k - 1):
            for j in range(i * k, (i + 1) * k):
                fh = (fh * BASE + (ord(word[j + m]) - ALPHABET_START)) % MODULO
            hit.add(fh)

        bh = 0
        base = 1
        hard = (n - 1) // k + 1
        res = hard
        if m != 0:
            for i in range(m):
                bh = (bh + (ord(word[n - i - 1]) - ALPHABET_START) * base) % MODULO
                base = (base * BASE) % MODULO
            hard -= 1
            if bh in hit:
                res = hard
        for i in range(n // k - 1):
            for j in range(i * k, (i + 1) * k):
                bh = (bh + (ord(word[n - j - m - 1]) - ALPHABET_START) * base) % MODULO
                base = (base * BASE) % MODULO
            hard -= 1
            if bh in hit:
                res = hard
        return res


if __name__ == '__main__':
    r = Solution().minimumTimeToInitialState(word="ababa", k=2)
    print(r)
