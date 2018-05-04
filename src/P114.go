package leetcode

var last *TreeNode

func doFlattern(cur *TreeNode) {
	if cur == nil {
		return
	}
	if last != nil {
		last.Left = cur
	}
	last = cur
	doFlattern(cur.Left)
	doFlattern(cur.Right)

}

func reverseTree(cur *TreeNode) {
	if cur == nil {
		return
	}

	cur.Right = cur.Left
	reverseTree(cur.Left)
	cur.Left = nil
}

func flatten(root *TreeNode) {
	doFlattern(root)
	reverseTree(root)
}
