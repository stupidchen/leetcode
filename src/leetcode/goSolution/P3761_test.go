package goSolution

import "testing"

func TestMaximumGap(t *testing.T) {
	nums := []int {1, 4}
	AssertEqual(t, 3, maximumGap(nums))
}
