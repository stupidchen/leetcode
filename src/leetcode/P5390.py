S = 'croak'


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = [0] * len(S)
        r = 0
        for c in croakOfFrogs:
            d[S.find(c)] += 1
            for i in range(1, len(S)):
                if d[i] > d[i - 1]:
                    return -1
            r = max(r, d[0] - d[1], d[0] - d[2], d[0] - d[3], d[0] - d[4])
        if all(d[i] == d[0] for i in range(len(S))):
            return r
        else:
            return -1


if __name__ == '__main__':
    print(Solution().minNumberOfFrogs('crcoakroak'))
