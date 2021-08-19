from functools import lru_cache
from typing import Optional

MOD = 10 ** 9 + 7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        @lru_cache(maxsize=None)
        def get_sum(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return node.val + get_sum(node.left) + get_sum(node.right)

        sum_of_tree = get_sum(root)

        def get_max_product(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            sum_of_subtree = get_sum(node)
            return max(get_max_product(node.left), get_max_product(node.right),
                       sum_of_subtree * (sum_of_tree - sum_of_subtree))
        return get_max_product(root) % MOD
