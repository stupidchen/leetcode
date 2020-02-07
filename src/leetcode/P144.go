package leetcode

func solvePreorderTraversal(current *TreeNode, preorder []int, pos *int) {
	if current == nil {
		return
	}

	preorder[*pos] = current.Val
	*pos++
	solvePreorderTraversal(current.Left, preorder, pos)
	solvePreorderTraversal(current.Right, preorder, pos)
}

func preorderTraversal(root *TreeNode) []int {
	var ret [10000]int
	var n = 0

	solvePreorderTraversal(root, ret[: ], &n)
	return ret[: n]
}