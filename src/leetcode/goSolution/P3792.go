package goSolution

func countSmaller(nums []int) []int {
	minNum := min(nums...)
	maxNum := max(nums...)
	ft := NewFenwickTree(maxNum - minNum + 1)
	n := len(nums)
	ret := make([]int, len(nums))
	for i := n - 1; i >= 0; i-- {
		c := nums[i] - minNum + 1
		ret[i] = ft.get(c - 1, func(v, d int) int {
			return v + d
		})
		ft.update(c, func(d int) int {
			return d + 1
		})
	}
	return ret
}
