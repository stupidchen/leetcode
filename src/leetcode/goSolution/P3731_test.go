package goSolution

import "testing"

func TestCheckPossibility(t *testing.T) {
	nums := []int {4, 2, 1}
	AssertEqual(t, false, checkPossibility(nums))
}
