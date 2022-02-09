from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s = set()
        for edge in edges:
            for node in edge:
                if node in s:
                    return node
                s.add(node)

