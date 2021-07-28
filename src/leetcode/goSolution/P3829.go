package goSolution

func beautifulArray(n int) []int {
	if n == 1 {
		return []int{1}
	}
	left := beautifulArray((n + 1) >> 1)
	right := beautifulArray(n >> 1)
	for i, v := range left {
		left[i] = (v << 1) - 1
	}
	for i, v := range right {
		right[i] = v << 1
	}
	return append(left, right...)
}
