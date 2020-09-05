# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1, root2):
        def numbers(node):
            if node is None:
                return []
            return numbers(node.left) + [node.val] + numbers(node.right)

        a1 = numbers(root1)
        a2 = numbers(root2)
        return list(sorted(a1 + a2))
