package leetcode

func rangeBitwiseAnd(m int, n int) int {
	var i uint
	var ret = 0
	for i = 0; (1 << i) <= n; i++ {
		t := 1 << i
		if (m | t) == m && (n | t) == n {
			if n - m < t {
				ret += t
			}
		}
	}

	return ret
}