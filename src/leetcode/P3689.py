class Solution:
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """

        tree_voyage = []

        def get_voyage(node):
            if node is None:
                return
            tree_voyage.append(node.val)
            setattr(node, 'index', len(tree_voyage) - 1)
            get_voyage(node.left)
            get_voyage(node.right)

        def match_voyage(node, t_voyage, tl, tr, vl, vr):
            if tl == tr:
                return voyage[vl] == t_voyage[tl] and vl == vr, []

            if t_voyage[tl] != voyage[vl]:
                return False, []

            if node.left is None:
                return match_voyage(node.right, t_voyage, tl + 1, tr, vl + 1, vr)
            if node.right is None:
                return match_voyage(node.left, t_voyage, tl + 1, tr, vl + 1, vr)

            t = node.right.index - node.index
            l_s, l_f = match_voyage(node.left, t_voyage, tl + 1, tl + t - 1, vl + 1, vl + t - 1)
            r_s, r_f = match_voyage(node.right, t_voyage, tl + t, tr, vl + t, vr)
            if l_s and r_s:
                return True, l_f + r_f

            l_s, l_f = match_voyage(node.left, t_voyage, tl + 1, tl + t - 1, vr - t + 2, vr)
            r_s, r_f = match_voyage(node.right, t_voyage, tl + t, tr, vl + 1, vr - t + 1)
            if l_s and r_s:
                return True, [node.val] + l_f + r_f
            return False, []

        get_voyage(root)
        if len(tree_voyage) != len(voyage):
            return [-1]
        solved, flip = match_voyage(root, tree_voyage, 0, len(tree_voyage) - 1, 0, len(tree_voyage) - 1)
        if solved:
            return flip
        return [-1]
