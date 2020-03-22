def count(x):
    if x == 1:
        return 1, 1
    if x == 2:
        return 2, 3
    r = 0
    s = 0
    for i in range(1, x):
        t = x // i
        if t < i:
            break
        if x % i == 0:
            r += 1
            s += i
            if t != i:
                r += 1
                s += t

    return r, s


class Solution:
    def sumFourDivisors(self, nums) -> int:
        r = 0
        for num in nums:
            d, s = count(num)
            if d == 4:
                r += s
        return r


if __name__ == '__main__':
    print(Solution().sumFourDivisors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
