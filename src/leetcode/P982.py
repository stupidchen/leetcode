from collections import defaultdict


class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        d = defaultdict(lambda: 0)
        for a in A:
            for b in A:
                d[a & b] += 1

        ret = 0
        for a in A:
            for b in d.keys():
                if a & b == 0:
                    ret += d[b]

        return ret


if __name__ == '__main__':
    print(Solution().countTriplets([2, 4, 7, 3]))
    # print(Solution().countTriplets([2, 1, 3]))
