class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        sequence += '$' * (len(word))
        n = len(sequence)
        m = len(word)
        r = 0
        for i in range(n):
            for j in range((n - i + 1) // m):
                if sequence[i + j * m: i + (j + 1) * m] != word:
                    r = max(r, j)
                    break
        return r


if __name__ == '__main__':
    print(Solution().maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
