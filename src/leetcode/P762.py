from math import floor, sqrt


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        r = 0
        for i in range(left, right + 1):
            t = bin(i).count('1')
            if is_prime(t):
                r += 1
        return r


if __name__ == '__main__':
    print(Solution().countPrimeSetBits(10, 15))
