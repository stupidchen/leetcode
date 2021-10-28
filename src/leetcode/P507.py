from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = set()
        for i in range(int(sqrt(num))):
            d = i + 1
            r, m = divmod(num, d)
            if m == 0:
                divisors.add(r)
                divisors.add(d)
        return sum(divisors) - num == num


if __name__ == '__main__':
    print(Solution().checkPerfectNumber(28))
