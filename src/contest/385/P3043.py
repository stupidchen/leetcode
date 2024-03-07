from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie_root = {}
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        for i in arr1:
            trie_node = trie_root
            for l in str(i):
                node = trie_node.get(l)
                if node is None:
                    node = {}
                    trie_node[l] = node
                    trie_node = node
                else:
                    trie_node = node

        ret = 0
        for i in arr2:
            trie_node = trie_root
            c = 0
            for l in str(i):
                node = trie_node.get(l)
                if node is None:
                    break
                else:
                    c += 1
                    trie_node = node
            ret = max(c, ret)
        return ret

