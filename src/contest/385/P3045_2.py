from collections import defaultdict
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = (T := lambda: defaultdict(T))()
        res = 0
        for word in words:
            node = root
            for prefix_letter, suffix_letter in zip(word, reversed(word)):
                res += (node := node[(prefix_letter, suffix_letter)]).get(0, 0)
            node[0] = node.get(0, 0) + 1
        return res


if __name__ == '__main__':
    r = Solution().countPrefixSuffixPairs(["a", "a"])
    print(r)


