package goSolution

func trap(height []int) int {
	n := len(height)
	lmax := make([]int, n + 1)
	rmax := make([]int, n + 1)
	for i := 0; i < n; i++ {
		lmax[i + 1] = max(lmax[i], height[i])
	}
	for i := n - 1; i >= 0; i-- {
		rmax[i] = max(rmax[i + 1], height[i])
	}
	ret := 0
	for i := 1; i < n; i++ {
		ret += max(min(lmax[i], rmax[i]) - height[i], 0)
	}
	return ret
}