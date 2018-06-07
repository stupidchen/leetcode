package leetcode

func countBit(m int, n uint) int {
	if 1 << n <= m {
		return m - (1 << n)
	}
	return 0
}

func rangeBitwiseAnd(m int, n int) int {
	var i uint
	var ret = 0
	for i = 0; (1 << i) <= n; i++ {
		t := countBit(n, i) - countBit(m, i)
		if (t & 1) == 1 {
			ret = ret | (1 << i)
		}
	}

	return ret
}