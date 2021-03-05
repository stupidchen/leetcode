# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        ret = []
        ret_nodes = []

        def cal(node, depth):
            if node is None:
                return

            if len(ret) <= depth:
                ret.append(0)
                ret_nodes.append(0)
            ret[depth] += node.val
            ret_nodes[depth] += 1
            cal(node.left, depth + 1)
            cal(node.right, depth + 1)

        cal(root, 0)
        for i, v in enumerate(ret):
            ret[i] = v / ret_nodes[i]
        return ret
