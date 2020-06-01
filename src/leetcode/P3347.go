package leetcode

func doInvert(cur *TreeNode) {
	if cur == nil {
		return
	}
	var tmp = cur.Left
	cur.Left = cur.Right
	cur.Right = tmp
	doInvert(cur.Left)
	doInvert(cur.Right)
}

func invertTree(root *TreeNode) *TreeNode {
	doInvert(root)
	return root
}