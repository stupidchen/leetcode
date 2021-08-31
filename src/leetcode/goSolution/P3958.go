package goSolution

func findMin(nums []int) int {
	var l = 0
	var r = len(nums) - 1
	var mid int
	for ; l != r;  {
		mid = (l + r) >> 1
		if nums[l] <= nums[r] {
			break
		} else {
			if nums[mid] >= nums[l] {
				l = mid + 1
			} else {
				r = mid
			}
		}
	}

	return nums[l]
}