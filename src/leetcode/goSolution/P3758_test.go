package goSolution

import "testing"

func TestMaximumUniqueSubarray(t *testing.T) {
	nums := []int {5,2,1,2,5,2,1,2,5}
	AssertEqual(t, 8, maximumUniqueSubarray(nums))
}
