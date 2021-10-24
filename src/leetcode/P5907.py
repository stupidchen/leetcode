from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        t = n
        while True:
            t += 1
            c = Counter(str(t))
            v = True
            for i, k in c.items():
                if int(i) != k:
                    v = False
                    break
            if v:
                break
        return t


if __name__ == '__main__':
    print(Solution().nextBeautifulNumber(1000000))
