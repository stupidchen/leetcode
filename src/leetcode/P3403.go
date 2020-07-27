func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(postorder) == 0 {
		return nil
	}
	if len(postorder) == 1 {
		return &TreeNode{Val: postorder[0]}
	}
	var n = len(postorder)
	var c = TreeNode{Val: postorder[n - 1]}
	for i := 0; i < len(inorder); i++ {
		if inorder[i] == postorder[n - 1] {
			c.Left = buildTree(inorder[: i], postorder[0: i])
			c.Right = buildTree(inorder[i + 1: ], postorder[i: n - 1])
			break
		}
	}
	return &c
}
