class Solution:
    def solve(self, root, sum, p):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            if root.val == sum:
                return 1
            return 0

        ret = self.solve(root.left, sum - root.val, True) + \
              self.solve(root.right, sum - root.val, True)
        if sum == root.val:
            ret += 1
        if not p:
            ret += self.solve(root.left, sum, False) + self.solve(root.right, sum, False)
        return ret

    def pathSum(self, root, sum):
        return self.solve(root, sum, False)

