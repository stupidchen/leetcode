package goSolution

import (
	"testing"
)

func TestNormalCase(t *testing.T) {
	root := &Node{Val: 1, Children: []*Node{&Node{Val: 2}, &Node{Val: 3}, &Node{Val: 4}}}
	AssertEqual(t, preorder(root), []int{1, 2, 3, 4})
}

func TestEmptyRoot(t *testing.T) {
	AssertEqual(t, preorder(nil), []int{})
}
