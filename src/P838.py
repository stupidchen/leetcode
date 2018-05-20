class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """

        dominoes = list(dominoes)
        last = None

        for i in range(len(dominoes)):
            if dominoes[i] == 'L':
                if last is not None and dominoes[last] == 'L':
                    for j in range(last, i):
                        dominoes[j] = 'L'
                    last = i
                    continue
                if last is None:
                    for j in range(i):
                        dominoes[j] = 'L'
                else:
                    t = i
                    while last < t:
                        dominoes[last] = 'R'
                        dominoes[t] = 'L'
                        last += 1
                        t -= 1
                    if last == t:
                        dominoes[t] = '.'
                last = i
            if dominoes[i] == 'R':
                if last is not None and dominoes[last] == 'R':
                    for j in range(last, i):
                        dominoes[j] = 'R'
                last = i

        if last is not None and dominoes[last] == 'R':
            for i in range(last, len(dominoes)):
                dominoes[i] = 'R'

        ret = ""
        for i in dominoes:
            ret += i
        return ret
