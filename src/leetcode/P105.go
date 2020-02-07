package leetcode

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	if len(preorder) == 1 {
		return &TreeNode{Val: preorder[0]}
	}
	var c = TreeNode{Val: preorder[0]}
	for i := 0; i < len(inorder); i++ {
		if inorder[i] == preorder[0] {
			c.Left = buildTree(preorder[1: i + 1], inorder[: i])
			c.Right = buildTree(preorder[i + 1: ], inorder[i + 1: ])
			break
		}
	}
	return &c
}