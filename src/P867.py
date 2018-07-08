import math


def xn_mod_p2(x, n, p):
    res = 1
    n_bin = bin(n)[2:]
    for i in range(0, len(n_bin)):
        res = res ** 2 % p
        if n_bin[i] == '1':
            res = res * x % p
    return res


def miller_rabin_witness(a, p):
    if p == 1:
        return False
    if p == 2:
        return True
    # p-1 = u*2^t 求解 u, t
    n = p - 1
    t = int(math.floor(math.log(n, 2)))
    u = 1
    while t > 0:
        u = n // 2 ** t
        if n % 2 ** t == 0 and u % 2 == 1:
            break
        t = t - 1
    b1 = b2 = xn_mod_p2(a, u, p)
    for i in range(1, t + 1):
        b2 = b1 ** 2 % p
        if b2 == 1 and b1 != 1 and b1 != (p - 1):
            return False
        b1 = b2
    if b1 != 1:
        return False
    return True


F = [2, 7, 61]


def prime_test_miller_rabin(p):
    if p == 1:
        return False
    for a in F:
        if a >= p:
            break
        if not miller_rabin_witness(a, p):
            return False
    return True


class Solution(object):
    F = [2, 7, 61]

    def primePalindrome(self, N):
        s = str(N)
        l = len(s)
        i = l
        while 1:
            t = (i + 1) >> 1
            if i == l:
                h = s[: t]
            else:
                h = '1' + '0' * (t - 1)
            j = h
            while 1:
                l2 = len(h)
                if l2 > t:
                    break
                p = h
                if l2 << 1 > i:
                    p += h[::-1][1:]
                else:
                    p += h[::-1]
                pi = int(p)
                if pi >= N and prime_test_miller_rabin(pi):
                    return pi
                h = str(int(h) + 1)
            i += 1


if __name__ == '__main__':
    print(Solution().primePalindrome(6))
