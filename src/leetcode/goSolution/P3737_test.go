package goSolution

import "testing"

func TestIsPossible(t *testing.T) {
	nums := []int {9, 3, 5}
	AssertEqual(t, true, isPossible(nums))

	nums = []int {1, 1000000000}
	AssertEqual(t, true, isPossible(nums))
}
