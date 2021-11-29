class Solution:
    def minDiffInBST(self, root) -> int:
        def order(node):
            if node is None:
                return []
            return order(node.left) + [node.val] + order(node.right)

        order_list = order(root)
        return min([order_list[i] - order_list[i - 1] for i in range(1, len(order_list))])
