class Solution:
    def stringMatching(self, words):
        r = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if words[j].find(words[i]) != -1:
                        r.append(words[i])
                        break

        return r


if __name__ == '__main__':
    print(Solution().stringMatching(["blue","green","bu"]))
