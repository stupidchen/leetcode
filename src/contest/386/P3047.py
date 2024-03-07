from typing import List


def overlap(s1, e1, s2, e2):
    if s1 <= s2 <= e1:
        return min(e1 - s2, e2 - s2)
    elif s1 <= e2 <= e1:
        return min(e2 - s1, e2 - s2)
    elif s2 <= s1 <= e2:
        return min(e2 - s1, e1 - s1)
    elif s2 <= e1 <= e2:
        return min(e1 - s2, e1 - s1)

    return 0


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        r = 0
        for i in range(n):
            for j in range(i + 1, n):
                h = overlap(bottomLeft[i][0], topRight[i][0], bottomLeft[j][0], topRight[j][0])
                w = overlap(bottomLeft[i][1], topRight[i][1], bottomLeft[j][1], topRight[j][1])
                s = min(h, w)
                r = max(s * s, r)
        return r


if __name__ == '__main__':
    print(Solution().largestSquareArea([[2, 1], [4, 15], [17, 6], [19, 5]],
                                       [[3, 17], [10, 23], [23, 11], [22, 13]]))
