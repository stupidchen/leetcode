def valid(d):
    return all(map(lambda x: x > 0, d.values()))


class Solution:
    def numberOfSubstrings(self, s):
        d = {'a': 0, 'b': 0, 'c': 0}
        s += '$'
        n = len(s)
        l, r = 0, 0
        for i in range(n):
            while valid(d):
                d[s[l]] -= 1
                r += n - i
                l += 1

            if s[i] != '$':
                d[s[i]] += 1
        return r


# For test only
SI = (("abcabc",), ("aaacb",))
SO = (10, 3)
TM = 'numberOfSubstrings'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
