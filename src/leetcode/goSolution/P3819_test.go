package goSolution

import "testing"

func TestLowestCommonAncestor(t *testing.T) {
	root := TreeNode{Val: 6, Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 0}, Right: &TreeNode{Val: 4}}, Right: &TreeNode{Val: 8}}

	AssertEqual(t, 2, lowestCommonAncestor(&root, &TreeNode{Val: 0}, &TreeNode{Val: 4}).Val)
}
