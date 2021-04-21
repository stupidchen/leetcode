package goSolution

import "math"

func min(vars ...int) int {
	r := vars[0]
	for i := 1; i < len(vars); i++ {
		if r > vars[i] {
			r = vars[i]
		}
	}
	return r
}

func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	for i := 1; i < n; i++ {
		for j := 0; j < i + 1; j++ {
			k := math.MaxInt64
			if j > 0 {
				k = min(k, triangle[i - 1][j - 1] + triangle[i][j])
			}
			if j < i {
				k = min(k, triangle[i - 1][j] + triangle[i][j])
			}
			triangle[i][j] = k
		}
	}

	return min(triangle[n - 1]...)
}
