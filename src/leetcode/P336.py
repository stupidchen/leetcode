from copy import deepcopy


class TrieNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = {}


class Trie(object):
    def __init__(self, init_val=None):
        self.root = TrieNode(deepcopy(init_val))
        self.init_val = init_val

    def insert(self, string, value, insert_on_path=False, reduce_func=lambda x, y: y):
        i, n = 0, len(string)
        node = self.root
        while i < n:
            if string[i] not in node.next:
                node.next[string[i]] = TrieNode(deepcopy(self.init_val))

            if insert_on_path:
                node.val = reduce_func(node.val, value)
            node = node.next[string[i]]

            i += 1
        node.val = reduce_func(node.val, value)

    def get(self, string, reduce_func=lambda x, y: y, init_val=None):
        i, n = 0, len(string)
        node = self.root
        v = init_val
        while i < n:
            if string[i] not in node.next:
                return False, v
            v = reduce_func(v, node.val)
            node = node.next[string[i]]
            i += 1

        v = reduce_func(v, node.val)
        return True, v


def isPalindrome(s, l=0, r=None):
    if r is None:
        r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


class Solution:
    def palindromePairs(self, words):
        trie = Trie(None)
        n = len(words)
        for i in range(n):
            trie.insert(words[i][::-1], i)
        r = []
        for i in range(n):
            m = len(words[i])
            for k in range(m + 1):
                f, p = trie.get(words[i][k:])
                if f and p is not None and i != p:
                    if isPalindrome(words[i], 0, k - 1) and m > len(words[p]):
                        r.append([p, i])
                f, p = trie.get(words[i][:k])
                if f and p is not None and i != p:
                    if isPalindrome(words[i], k):
                        r.append([i, p])
        return r


if __name__ == '__main__':
    print(Solution().palindromePairs(["abc", "ba"]))
    print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
