from collections import Counter


class Solution:
    def groupAnagrams(self, strs):
        ret = []
        d = {}
        for s in strs:
            c = tuple(sorted(zip(Counter(s).keys(), Counter(s).values())))
            if c not in d:
                d[c] = len(ret)
                ret.append([])

            t = d[c]
            ret[t].append(s)

        return ret


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
