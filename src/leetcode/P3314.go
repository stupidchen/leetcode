package leetcode

type TreeNodeWrapper struct {
	node *TreeNode
	left, right *TreeNodeWrapper
	f int
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func initWrapper(cur *TreeNode) *TreeNodeWrapper {
	if cur == nil {
		return nil
	}
	return &TreeNodeWrapper{node: cur, left: initWrapper(cur.Left), right: initWrapper(cur.Right)}
}

func solveOnePathSum(cur *TreeNodeWrapper) int {
	var l = 0
	var r = 0
	if cur.left != nil {
		l = max(0, solveOnePathSum(cur.left))
	}
	if cur.right != nil {
		r = max(0, solveOnePathSum(cur.right))
	}
	cur.f = cur.node.Val + max(l, r)
	return cur.f
}

func solveTwoPathSum(cur *TreeNodeWrapper) int {
	var t = cur.node.Val
	var ret = t
	if cur.left != nil {
		ret = max(ret, solveTwoPathSum(cur.left))
		t += max(0, cur.left.f)
	}
	if cur.right != nil {
		ret = max(ret, solveTwoPathSum(cur.right))
		t += max(0, cur.right.f)
	}
	ret = max(ret, t)
	return ret
}

func maxPathSum(root *TreeNode) int {
	var rootWrapper = initWrapper(root)
	solveOnePathSum(rootWrapper)
	return solveTwoPathSum(rootWrapper)
}