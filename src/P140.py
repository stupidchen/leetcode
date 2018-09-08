import re


class Solution:
    words = []

    def generate_solution(self, f, i, solution, solutions):
        if i < 0:
            solutions.append(solution[:-1])
            return
        for j in f[i]:
            word = self.words[j]
            self.generate_solution(f, i - len(word), word + ' ' + solution, solutions)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        if n == 0:
            return []
        select = [[] for i in range(n)]
        self.words = wordDict
        for i in range(len(self.words)):
            word = self.words[i]
            for m in re.finditer(r'(?=({}))'.format(word), s):
                t = m.end(1) - 1
                select[t].append(i)

        f = [[] for i in range(n)]
        for i in range(n):
            for j in select[i]:
                word = self.words[j]
                if i + 1 == len(word) or len(f[i - len(word)]) > 0:
                    f[i].append(j)

        ret = []
        self.generate_solution(f, n - 1, '', ret)
        return ret


if __name__ == '__main__':
    print(Solution().wordBreak('aaaaaaa', ["aaaa", "aaa"]))
