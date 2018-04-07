package leetcode

func getFactory(n int, f int) int {
	var ret = 0
	for ; n > 0; n /= f {
		ret += n / f
	}
	return ret
}

func trailingZeroes(n int) int {
	var f2 = getFactory(n, 2)
	var f5 = getFactory(n, 5)
	if f2 > f5 {
		return f5
	} else {
		return f2
	}
}