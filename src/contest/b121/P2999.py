class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        sl = len(s) - 1
        si = int(s)

        def f(n):
            lg = len(str(n)) - 1
            if lg < sl:
                return 0

            if lg == sl:
                return int(n >= si)

            base = 10 ** lg
            first, mod = divmod(n, 10 ** lg)
            res = f(base - 1) * min(first, limit + 1) + f(mod) * int(first <= limit)
            return res

        return f(finish) - f(start - 1)


if __name__ == '__main__':
    r = Solution().numberOfPowerfulInt(start=1, finish=10 ** 15, limit=4, s="9")
    print(r)
