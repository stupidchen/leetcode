package goSolution

import "testing"

func TestSearchRangeNormalCase(t *testing.T) {
	nums := []int {5,7,7,8,8,10}
	AssertEqual(t, []int{3, 4}, searchRange(nums, 8))
}

func TestSearchRangeNormalCase2(t *testing.T) {
	nums := []int {5,7,7,8,8,10}
	AssertEqual(t, []int{-1, -1}, searchRange(nums, 6))
}
