def last_bit(x):
    return x ^ (x & (x - 1))


def count_bit(x):
    r = 0
    while x > 0:
        r += 1
        x -= last_bit(x)
    return r


class Solution:
    def readBinaryWatch(self, num: int):
        r = []
        for i in range(12):
            for j in range(60):
                if count_bit(i) + count_bit(j) == num:
                    h = str(i)
                    m = str(j)
                    if len(m) < 2:
                        m = '0' + m
                    r.append('{}:{}'.format(h, m))
        return r


if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))
