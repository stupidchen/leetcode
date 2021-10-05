import time
from typing import List


def last_bit(x):
    return x & (x ^ (x - 1))


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        m = len(s)
        ss = ''
        rp = lp = 0
        np = []
        d = [0] * m
        for i, c in enumerate(s):
            if c == '(' or c == ')':
                d[len(ss)] = i
                ss += c
                if c == '(':
                    lp += 1
                else:
                    rp += 1
            else:
                np.append(i)

        n = len(ss)
        if n == 0:
            return [s]
        b = {}
        for i in range(n):
            b[1 << i] = i
        lnp = len(np)
        l = [False] * n
        for i in range(n):
            if ss[i] == '(':
                l[i] = True
        sk = [0] * (n + 1)
        v = [0] * (n + 1)
        for i in range(n):
            v[i] = 1 if l[i] else -1
            sk[i + 1] = sk[i] + v[i]
        llb = n
        k = 0
        ret = []
        ret_m = n + 1
        for i in reversed(range(1 << n)):
            if i == 0:
                k = 0
            else:
                lb = b[last_bit(i)]
                k = k - v[llb] + sk[llb]
                llb = lb
            if k != 0:
                continue

            t = []
            kk = 0
            ti = i
            rc = n
            while ti != 0:
                j = last_bit(ti)
                idx = b[j]
                rc -= 1
                if l[idx]:
                    kk += 1
                else:
                    kk -= 1
                    if kk < 0:
                        break
                ti -= j
                t.append(d[idx])

            if kk != 0 or rc > ret_m:
                continue

            if ret_m > rc:
                ret_m = rc
                ret = []
            if ret_m == rc:
                ret.append(t)

        n_ret = set()
        for ids in ret:
            t = ''
            j = 0
            for i in ids:
                while j < lnp and i > np[j]:
                    t += s[np[j]]
                    j += 1
                t += s[i]
            while j < lnp:
                t += s[np[j]]
                j += 1
            n_ret.add(t)

        return list(n_ret)


if __name__ == '__main__':
    st = time.time()
    print(Solution().removeInvalidParentheses("()())()"))
    print(Solution().removeInvalidParentheses("p(r)"))
    print(Solution().removeInvalidParentheses("(a)())()"))
    print(Solution().removeInvalidParentheses("()((())h()(()()()))(("))
    et = time.time()
    print(et - st)
