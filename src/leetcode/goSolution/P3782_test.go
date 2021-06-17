package goSolution

import "testing"

func TestNumSubarrayBoundedMax(t *testing.T) {
	nums := []int {2, 1, 4, 3}
	AssertEqual(t, 3, numSubarrayBoundedMax(nums, 2, 3))
}
