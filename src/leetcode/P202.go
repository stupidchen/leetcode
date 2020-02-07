package leetcode

func nextSquareSum(n int) int {
	var ret = 0
	for ;n > 0; n /= 10 {
		var t = n % 10
		ret += t * t
	}
	return ret
}

func isHappy(n int) bool {
	var f [1000]bool
	n = nextSquareSum(n)
	for ; n != 1; n = nextSquareSum(n) {
		if f[n] {
			return false
		}
		f[n] = true
	}
	return true
}