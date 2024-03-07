from collections import Counter
from math import sqrt
from typing import List

directions = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1))


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        counter = Counter()
        for i in range(n):
            for j in range(m):
                num = mat[i][j]
                counter[num] += 1
                for direction in directions:
                    num = mat[i][j]
                    dx, dy = direction
                    for step in range(1, max(n, m)):
                        tx, ty = i + step * dx, j + step * dy
                        if not ((0 <= tx < n) and (0 <= ty < m)):
                            break
                        num = num * 10 + mat[tx][ty]
                        counter[num] += 1

        ret_number = -1
        ret_frequency = 0
        for number, frequency in counter.items():
            if number <= 10:
                continue
            is_prime = True
            if number == 1:
                is_prime = False
            else:
                for i in range(2, int(sqrt(number)) + 1):
                    if number % i == 0:
                        is_prime = False
                        break
            if not is_prime:
                continue

            if frequency > ret_frequency:
                ret_number = number
                ret_frequency = frequency
            elif frequency == ret_frequency and number > ret_number:
                ret_number = number
        return ret_number


if __name__ == '__main__':
    r = Solution().mostFrequentPrime([[9, 7, 8], [4, 6, 5], [2, 8, 6]])
    print(r)
