"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from itertools import chain
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        return list(chain(*[self.postorder(child) for child in root.children])) + [root.val]
