package goSolution

func runningSum(nums []int) []int {
	n := len(nums)
	ret := make([]int, n + 1)
	for i := 0; i < n; i++ {
		ret[i + 1] = ret[i] + nums[i]
	}
	return ret[1: ]
}
