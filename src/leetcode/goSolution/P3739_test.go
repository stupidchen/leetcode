package goSolution

import "testing"

func TestMaxScore(t *testing.T) {
	nums := []int {1, 2, 3, 4, 5, 6, 1}
	AssertEqual(t, 12, maxScore(nums, 3))
}
