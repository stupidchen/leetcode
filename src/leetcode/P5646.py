from collections import defaultdict
from math import inf


class Solution:
    def minimumTeachings(self, n: int, languages, friendships):
        s = set()
        sl = []
        for language in languages:
            for l in language:
                s.add(l)
            sl.append(set(language))

        r = inf
        for l in s:
            v = defaultdict(lambda: False)
            for x, y in friendships:
                x -= 1
                y -= 1
                if sl[x] & sl[y]:
                    continue
                if l not in sl[x]:
                    v[x] = True
                if l not in sl[y]:
                    v[y] = True
            r = min(len(v.keys()), r)
        return r


if __name__ == '__main__':
    print(Solution().minimumTeachings(17,
                                      [[4, 7, 2, 14, 6], [15, 13, 6, 3, 2, 7, 10, 8, 12, 4, 9], [16], [10], [10, 3],
                                       [4, 12, 8, 1, 16, 5, 15, 17, 13], [4, 13, 15, 8, 17, 3, 6, 14, 5, 10],
                                       [11, 4, 13, 8, 3, 14, 5, 7, 15, 6, 9, 17, 2, 16, 12], [4, 14, 6],
                                       [16, 17, 9, 3, 11, 14, 10, 12, 1, 8, 13, 4, 5, 6], [14], [7, 14],
                                       [17, 15, 10, 3, 2, 12, 16, 14, 1, 7, 9, 6, 4]],
                                      [[4, 11], [3, 5], [7, 10], [10, 12], [5, 7], [4, 5], [3, 8], [1, 5], [1, 6],
                                       [7, 8], [4, 12], [2, 4], [8, 9], [3, 10], [4, 7], [5, 12], [4, 9], [1, 4],
                                       [2, 8], [1, 2], [3, 4], [5, 10], [2, 7], [1, 7], [1, 8], [8, 10], [1, 9],
                                       [1, 10], [6, 7], [3, 7], [8, 12], [7, 9], [9, 11], [2, 5], [2, 3]]))
