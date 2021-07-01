package goSolution

func grayCode(n int) []int {
	ret := make([]int, 1 << n)
	for i := 0; i < 1 << n; i++ {
		ret[i] = i ^ (i >> 1)
	}
	return ret
}
