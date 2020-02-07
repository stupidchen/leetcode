class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        rd = {}
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = words[i]
            else:
                if d[pattern[i]] != words[i]:
                    return False
            if words[i] not in rd:
                rd[words[i]] = pattern[i]
            else:
                if rd[words[i]] != pattern[i]:
                    return False
        return True
