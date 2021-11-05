class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        m = max(nums)
        for i, v in enumerate(nums):
            if v == m:
                root = TreeNode(v)
                root.left = self.constructMaximumBinaryTree(nums[:i])
                root.right = self.constructMaximumBinaryTree(nums[i+1:])
                return root
