class Solution:
    def makeGood(self, s: str) -> str:
        def find(x):
            for i in range(len(x) - 1):
                if x[i].lower() == x[i + 1].lower():
                    if (x[i].islower() and x[i + 1].isupper()) or (x[i].isupper() and x[i + 1].islower()):
                        return i
            return -1

        while True:
            t = find(s)
            if t != -1:
                s = s[:t] + s[t+2:]
            else:
                break
        return s

