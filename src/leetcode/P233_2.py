from functools import lru_cache


@lru_cache(maxsize=None)
def number_of_one(n):
    if n <= 0:
        return 0
    if n <= 9:
        return 1

    unit = 10 ** (len(str(n)) - 1)
    tail = n % unit
    head = n // unit
    return number_of_one(n - tail - 1) + (number_of_one(tail) + (head == 1) * (tail + 1))


class Solution:
    def countDigitOne(self, n: int) -> int:
        return number_of_one(n)


if __name__ == '__main__':
    r = Solution().countDigitOne(255)
    print(r)
