from collections import defaultdict

class Solution:
    def pseudoPalindromicPaths(self, root):
        def isPalindrome(path):
            t = path.values()
            o = 0
            for i in t:
                if i & 1 == 1:
                    o += 1
            return o <= 1

        r = [0]

        def solve(node, path):
            path[node.val] += 1
            if node.left is None and node.right is None:
                if isPalindrome(path):
                    r[0] += 1

                path[node.val] -= 1
                return

            if node.left is not None:
                solve(node.left, path)
            if node.right is not None:
                solve(node.right, path)
            path[node.val] -= 1

        solve(root, defaultdict(lambda: 0))
        return r[0]
