from typing import List


def select(min_left, left, right, length):
    # select interval [l, r] with left < r <= right, min_left <= l < left and r - l == length
    max_r = min(left - 1 + length, right)
    min_r = max(left + 1, min_left + length)
    return max(0, max_r - min_r + 1)


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        res = [0] * n
        for i in range(1, n):
            t = i - 1
            dup = False
            res[t] = max(x + n - y - t, 0)
            if x == y:
                res[t] -= 1

            if y - x > 1:
                if i == 1:
                    dup = True
                ld = (y - x + 1) >> 1
                if i <= ld:
                    if i == ld and (y - x + 1) & 1 == 0:
                        res[t] += (y - x + 1) >> 1
                    else:
                        res[t] += y - x + 1

                mid = (x + y) >> 1
                res[t] += select(1, x, mid, i)
                if (x + y) - mid != mid:
                    res[t] += select(1, x, mid, i - 1)
                else:
                    res[t] += select(1, x, mid - 1, i - 1)

                mid = (x + y + 1) >> 1
                res[t] += select(-n, -y, -mid, i)
                if (x + y) - mid != mid:
                    res[t] += select(-n, -y, -mid, i - 1)
                else:
                    res[t] += select(-n, -y, -mid - 1, i - 1)

            res[t] = (res[t] - int(dup)) << 1
        return res


if __name__ == '__main__':
    r = Solution().countOfPairs(n=5, x=1, y=4)
    print(r)
