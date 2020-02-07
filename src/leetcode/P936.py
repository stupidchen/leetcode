def solved(target):
    for i in target:
        if i != '?':
            return False
    return True


def match(stamp, target, s, t, m):
    for i in range(m):
        if stamp[s + i] != target[t + i] and target[t + i] != '?':
            return False
    return True

class Solution:
    ans = []
    deal = False
    cached = {}

    def solve(self, stamp, target, c, n, m):
        if solved(target):
            self.deal = True

        if self.deal or c < 0:
            return

        self.cached[target] = False

        for i in range(n - m + 1):
            if match(stamp, target, 0, i, m) and (not solved(target[i: i + m])):
                self.ans[c] = i
                new_target = target[:i] + '?' * m + target[i + m:]
                if new_target not in self.cached:
                    self.solve(stamp, new_target, c - 1, n, m)
                if self.deal:
                    return

    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        n = len(target)
        self.ans = [-1] * n * 10
        self.solve(stamp, target, n * 10 - 1, n, len(stamp))
        if self.deal:
            for i in range(n * 10):
                if self.ans[i] != -1:
                    return self.ans[i:]
        return []


if __name__ == '__main__':
    print(Solution().movesToStamp('qxq', 'qxqxqxqqxqxqqxqxqxqqxqxqqqxqqxqqqxqqxxqxqqxqqqxqqq'))
