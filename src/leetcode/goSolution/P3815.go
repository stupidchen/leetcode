package goSolution

import "sort"

func triangleNumber(nums []int) int {
	sort.Ints(nums)

	n := len(nums)
	ret := 0
	for i:= 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			num := nums[i] + nums[j]
			k := sort.SearchInts(nums, num)
			ret += max(k - j - 1, 0)
		}
	}
	return ret
}