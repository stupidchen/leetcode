package leetcode

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func max(x int, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func solve(root *TreeNode) int {
	if root == nil {
		return 0
	}

	var l = 0
	var r = 0
	if root.Left != nil {
		l = solve(root.Left)
	}
	if root.Right != nil {
		r = solve(root.Right)
	}

	if l < 0 || r < 0 {
		return -1
	} else {
		if abs(l - r) <= 1 {
			return max(l, r) + 1
		} else {
			return -1
		}
	}
}

func isBalanced(root *TreeNode) bool {
	return solve(root) >= 0
}