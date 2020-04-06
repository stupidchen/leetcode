from collections import Counter


class Solution:
    def groupAnagrams(self, strs):
        d = sorted(strs, key=lambda x: sorted(Counter(x).items()))
        r = [[]]
        d.append('$')
        for i in range(len(d) - 1):
            r[-1].append(d[i])
            if Counter(d[i]) != Counter(d[i + 1]):
                r.append([])
        return r[:-1]


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
