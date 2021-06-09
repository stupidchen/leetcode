package goSolution

import "testing"

func TestMaxResult(t *testing.T) {
	nums := []int {1,-1,-2,4,-7,3}
	AssertEqual(t, 7, maxResult(nums, 2))
}
