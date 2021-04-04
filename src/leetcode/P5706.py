class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        if sentence1 == sentence2:
            return True

        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1

        for i in range(len(sentence1) + 1):
            l = 0
            while l < i and sentence2[l] == sentence1[l]:
                l += 1

            r = len(sentence1) - 1
            t = len(sentence2) - 1
            while r > i and sentence2[t] == sentence1[r]:
                r -= 1
                t -= 1
            if r == l and ((l + 1 < len(sentence2) and sentence2[l+1] == ' ') or (t - 1 >= 0 and sentence2[t-1] == ' ')):
                return True
        return False


if __name__ == '__main__':
    print(Solution().areSentencesSimilar("xD iP tqchblXgqvNVdi", "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi"))
    print(Solution().areSentencesSimilar(sentence1="a b", sentence2="c d a b"))
    print(Solution().areSentencesSimilar(sentence1="My name is Haley", sentence2="My Haley"))
