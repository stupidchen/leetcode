package leetcode


func maxProfit2(prices []int) int {
	var f, rf [100000]int
	var n = len(prices)
	for i := 1; i < n; i++ {
		t := prices[i] - prices[i - 1]
		f[i] = 0
		if f[i - 1] + t > 0 {
			f[i] = f[i - 1] + t
		}
	}

	for i := n - 1; i > 0; i-- {
		t := prices[i] - prices[i - 1]
		rf[i] = 0
		if rf[i + 1] + t > 0 {
			rf[i] = rf[i + 1] + t
		}
	}

	var ret = 0
	for i := 1; i < n; i++ {
		if f[i] + rf[i] > ret {
			ret = f[i] + rf[i]
		}
	}
	return ret
}