package goSolution

func candy(ratings []int) int {
	n := len(ratings)
	f := make([]int, n)
	f[0] = 1
	for i := 1; i < n; i++ {
		if ratings[i] > ratings[i - 1] {
			f[i] = f[i - 1] + 1
		} else {
			f[i] = 1
		}
	}

	rf := make([]int, n)
	rf[n - 1] = 1
	for i := n - 2; i >= 0; i-- {
		if ratings[i] > ratings[i + 1] {
			rf[i] = rf[i + 1] + 1
		} else {
			rf[i] = 1
		}
	}

	ret := 0
	for i := 0; i < n; i++ {
		ret += max(f[i], rf[i])
	}
	return ret
}
