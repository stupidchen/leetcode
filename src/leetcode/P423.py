from collections import Counter

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
orders = [(0, 'z'), (6, 'x'), (7, 's'), (5, 'v'), (4, 'f'), (3, 'r'), (8, 'h'), (9, 'i'), (2, 'w'), (1, 'o')]


class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        f = [0] * 10
        for order in orders:
            n, i = order
            f[n] = c[i]
            for cc in digits[n]:
                c[cc] -= f[n]

        ret = ''
        for i in range(10):
            ret += str(i) * f[i]
        return ret


if __name__ == '__main__':
    print(Solution().originalDigits("owoztneoer"))
