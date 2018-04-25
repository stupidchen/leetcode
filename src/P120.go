package leetcode

func min(x int, y int) int {
	if x > y {
		return y
	}
	return x
}

func minimumTotal(triangle [][]int) int {
	var f [2][10000]int
	var n = len(triangle)
	for i := 0; i < n; i++ {
		for j := 0; j <= i; j++ {
			f[i & 1][j] = 0x7FFFFFFF
			if i == 0 || j < i {
				f[i & 1][j] = f[1 - (i & 1)][j] + triangle[i][j]
			}
			if j > 0 {
				f[i & 1][j] = min(f[1 - (i & 1)][j - 1] + triangle[i][j], f[i & 1][j])
			}
		}
	}

	var ans = f[1 - (n & 1)][0]
	for i := 1; i < n; i++ {
		ans = min(ans, f[1 - (n & 1)][i])
	}

	return ans
}
