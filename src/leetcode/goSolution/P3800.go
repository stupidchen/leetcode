package goSolution

import (
	"math"
	"sort"
)

func findClosestElements(arr []int, k int, x int) []int {
	n := len(arr)
	i := sort.SearchInts(arr, x)
	l, r := i, i + 1
	pick := make([]bool, n)
	for i := 0; i < k; i++ {
		if l < 0 {
			pick[r] = true
			r += 1
			continue
		}
		if r >= n {
			pick[l] = true
			l -= 1
			continue
		}
		dl := math.Abs(float64(arr[l] - x))
		dr := math.Abs(float64(arr[r] - x))
		if dl <= dr {
			pick[l] = true
			l -= 1
		} else {
			pick[r] = true
			r += 1
		}
	}
	ret := make([]int, 0)
	for i := 0; i < n; i++ {
		if pick[i] {
			ret = append(ret, arr[i])
		}
	}
	return ret
}
