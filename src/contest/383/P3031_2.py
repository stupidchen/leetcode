class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        f = [0] * n
        matched = 0
        for i in range(1, n):
            while matched > 0 and word[matched] != word[i]:
                matched = f[matched - 1]
            if word[matched] == word[i]:
                matched += 1
            f[i] = matched

        res = f[n - 1]
        while res > 0 and (n - res) % k != 0:
            res = f[res - 1]
        return (n - res - 1) // k + 1


if __name__ == '__main__':
    r = Solution().minimumTimeToInitialState(word="aab", k=2)
    print(r)
