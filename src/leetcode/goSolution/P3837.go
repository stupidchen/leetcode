package goSolution

import "sort"

func searchSubsetsWithDup(nums []int, pick []bool, current int, result *[][]int) {
	n := len(nums)
	if current == n {
		set := make([]int, 0)
		for i := 0; i < n; i++ {
			if pick[i] {
				set = append(set, nums[i])
			}
		}
		*result = append(*result, set)
		return
	}

	if !(current > 0 && nums[current - 1] == nums[current] && !pick[current - 1]) {
		pick[current] = true
		searchSubsetsWithDup(nums, pick, current + 1, result)
		pick[current] = false
	}
	searchSubsetsWithDup(nums, pick, current + 1, result)
}

func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	var result [][]int
	searchSubsetsWithDup(nums, make([]bool, n), 0, &result)
	return result
}