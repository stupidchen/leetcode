func min(x int, y int) int {
	if x > y {
		return y
	}
	return x
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	} else {
		var l = minDepth(root.Left)
		var r = minDepth(root.Right)
		if l == 0 {
			return r + 1
		}
		if r == 0 {
			return l + 1
		}
		return min(l, r) + 1
	}
}