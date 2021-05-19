package goSolution

import (
	"math"
	"sort"
)

func minMoves2(nums []int) int {
	sort.Ints(nums)
	ret := 0
	n := len(nums)
	t := nums[n / 2]
	for _, num := range nums {
		ret += int(math.Abs(float64(num) - float64(t)))
	}

	return ret
}
