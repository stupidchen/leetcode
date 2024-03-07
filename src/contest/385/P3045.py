from collections import Counter
from typing import List


class TrieNode:
    def __init__(self):
        self.child = {}
        self.value = Counter()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for letter in word:
            next_node = node.child.get(letter)
            if next_node is None:
                next_node = TrieNode()
                node.child[letter] = next_node
                node = next_node
            else:
                node = next_node
            node.value[word] += 1

    def find(self, word):
        node = self.root
        for letter in word:
            node = node.child.get(letter)
            if node is None:
                return {}
        return node.value



class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        ret = 0
        for word in reversed(words):
            candidates = trie.find(word)
            for candidate, number in candidates.items():
                if len(word) <= len(candidate) and candidate.endswith(word):
                    ret += number
            trie.add(word)
        return ret


if __name__ == '__main__':
    r = Solution().countPrefixSuffixPairs(["a", "a"])
    print(r)
