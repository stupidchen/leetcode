from collections import defaultdict


class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        d = defaultdict(lambda: 0)
        n = len(A)
        for a in A:
            t = 0
            for i in reversed(range(17)):
                if a | (1 << i) != a:
                    t += 1 << i
            d[t] += 1
        ret = 0
        for i in range(n):
            for j in range(n):
                t = (1 << 17) - 1 - A[i] & A[j]
                ret += d[t]


        return ret


if __name__ == '__main__':
    print(Solution().countTriplets([2, 4, 7, 3]))
    # print(Solution().countTriplets([2, 1, 3]))
