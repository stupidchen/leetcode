def next_hs(s):
    if s == '':
        return s
    n = len(s)
    f = False
    p = -1
    c = 1
    for i in reversed(range(n)):
        if s[i] != 'c':
            if i == 0:
                f = True
                c = 1
            else:
                for j in range(1, 3):
                    t = chr(ord(s[i]) + j)
                    if t <= 'c' and t != s[i - 1]:
                        f = True
                        c = j
                        break
            if f:
                p = i
                break
    if not f:
        return ''
    else:
        r = s[:p] + chr(c + ord(s[p]))
        for i in range(n - len(r)):
            r += chr(ord('a') + (i & 1))
        return r


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        r = ''
        for i in range(n):
            r += chr(ord('a') + (i & 1))

        for i in range(k - 1):
            r = next_hs(r)
        return r


if __name__ == '__main__':
    print(Solution().getHappyString(10, 100))
