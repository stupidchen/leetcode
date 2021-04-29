package goSolution

import "sort"

func searchRange(nums []int, target int) []int {
	l := sort.SearchInts(nums, target)
	r := sort.SearchInts(nums, target + 1)
	if (0 > l || l >= len(nums)) || nums[l] != target {
		return []int{-1, -1}
	} else {
		return []int{l, r - 1}
	}
}
