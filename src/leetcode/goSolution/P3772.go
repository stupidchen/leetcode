package goSolution

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}

	rootVal := preorder[0]
	root := TreeNode{Val: rootVal}
	for i := 0; i < len(inorder); i++ {
		if inorder[i] == rootVal {
			root.Left = buildTree(preorder[1:i+1], inorder[:i])
			root.Right = buildTree(preorder[i+1:], inorder[i+1:])
		}
	}
	return &root
}
