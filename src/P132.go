package leetcode

import "fmt"

func minCut(s string) int {
	var n = len(s)
	if n <= 1 {
		return 0
	}
	var p = make([]int, n)
	var f = make([][]bool, n)
	for i := 0; i < n; i++ {
		f[i] = make([]bool, n)
		f[i][i] = true
		if i < n - 1 {
			if s[i] == s[i + 1] {
				f[i][i + 1] = true
			} else {
				f[i][i + 1] = false
			}
		}
	}
	for i := 2; i < n; i++ {
		for j := 0; j + i < n; j++ {
			if s[j] == s[i + j] && f[j + 1][i + j - 1] {
				f[j][i + j] = true
			} else {
				f[j][i + j] = false
			}
		}
	}

	p[0] = 0
	for i := 1; i < n; i++ {
		if f[0][i] {
			p[i] = 0
		} else {
			p[i] = i
		}
		for j := i; j > 0; j-- {
			if f[j][i] && p[j - 1] + 1 < p[i] {
				p[i] = p[j - 1] + 1
			}
		}
	}
	return p[n - 1]
}

func main() {
	fmt.Println(minCut("aab"))
}