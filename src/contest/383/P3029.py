def is_matched(x, y):
    for cx, cy in zip(x, y):
        if not (cx == cy or cy == '#'):
            return False
    return True


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        res = 1
        current = word[k:] + '#' * k
        while not is_matched(word, current):
            res += 1
            current = current[k:] + '#' * k
        return res


if __name__ == '__main__':
    r = Solution().minimumTimeToInitialState(word="abacaba", k=3)
    print(r)
