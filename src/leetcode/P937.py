import re

NUMBER = re.compile('\d+')


def sort_key(s):
    letters = s.split()
    return ' '.join(letters[1:]) + letters[0]


class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        d = []
        l = []
        for log in logs:
            letters = log.split(' ')
            if NUMBER.match(letters[1]):
                d.append(log)
            else:
                l.append(log)

        l.sort(key=sort_key)
        return l + d


if __name__ == '__main__':
    print(Solution().reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
