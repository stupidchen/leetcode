package goSolution

import "testing"

func TestSubsetsWithDup(t *testing.T) {
	nums := []int {1, 2, 2}
	AssertEqual(t, 6, len(subsetsWithDup(nums)))
}
