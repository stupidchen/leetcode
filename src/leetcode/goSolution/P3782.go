package goSolution

func numSubarrayBoundedMax(nums []int, left int, right int) int {
	leftBoundary := -1
	rightBoundary := -1
	ret := 0
	for i, v := range nums {
		if v >= left {
			leftBoundary = i
		}
		if v > right {
			rightBoundary = i
		}
		ret += leftBoundary - rightBoundary
	}

	return ret
}
