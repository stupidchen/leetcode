class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        n = len(words)
        for i in range(n):
            t = words[i]
            r = ''
            for j in t:
                r += chr(order.find(j) + 97)
            words[i] = r
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] > words[j]:
                    return False
        return True
