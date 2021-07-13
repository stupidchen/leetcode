package goSolution

func findPeakElement(nums []int) int {
	n := len(nums)
	for i, num := range nums {
		if (i > 0 && num > nums[i - 1]) || i == 0 {
			if (i < n - 1 && num > nums[i + 1]) || i == n - 1 {
				return i
			}
		}
	}
	return -1
}
