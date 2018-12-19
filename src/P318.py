class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ret = 0
        n = len(words)
        b = [0]* n
        for i in range(n):
            for c in words[i]:
                b[i] |= (1 << (ord(c) - ord('a')))
        for i in range(n):
            for j in range(i + 1, n):
                if b[i] & b[j] == 0:
                    if len(words[i]) * len(words[j]) > ret:
                        ret = len(words[i]) * len(words[j])
        return ret
