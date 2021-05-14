package goSolution

import "testing"

func TestFlatten(t *testing.T) {
	root := &TreeNode{Left: &TreeNode{Left: &TreeNode{Val: 3}, Right: &TreeNode{Val: 4}, Val: 2}, Right: &TreeNode{Right: &TreeNode{Val: 6}, Val: 5}, Val: 1}
	flatten(root)
	for i := 1; i <= 6; i++ {
		AssertEqual(t, i, root.Val)
		root = root.Right
	}
}
