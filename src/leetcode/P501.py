class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def find(node: TreeNode) -> Dict:
            if node is None:
                return {}
            rr, rl = find(node.right), find(node.left)
            if node.val not in rr:
                rr[node.val] = 1
            else:
                rr[node.val] += 1
            for k, v in rl.items():
                if k not in rr:
                    rr[k] = v
                else:
                    rr[k] += v
            return rr
        d = find(root)
        m = max(list(d.values()) + [0])
        r = []
        for k, v in d.items():
            if v == m:
                r.append(k)
        return r
