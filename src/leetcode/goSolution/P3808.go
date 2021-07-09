package goSolution

import (
	"math"
	"sort"
)

func lengthOfLIS(nums []int) int {
	n := len(nums)
	f := make([]int, n)
	s := make([]int, n + 1)
	s[0] = math.MinInt64
	for i := 1; i <= n; i++ {
		s[i] = math.MaxInt64
	}

	ret := 0
	for i := 0; i < n; i++ {
		num := nums[i]
		t := sort.Search(n, func(i int) bool {
			k := n - i
			if s[k] < num {
				return true
			}
			return false
		})
		f[i] = n - t + 1
		s[f[i]] = min(s[f[i]], num)
		ret = max(ret, f[i])
	}
	return ret
}