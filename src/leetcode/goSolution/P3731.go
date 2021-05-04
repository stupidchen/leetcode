package goSolution

func _checkPossibility(nums []int) bool {
	for i := 1; i < len(nums); i++ {
		if nums[i] < nums[i - 1] {
			return false
		}
	}

	return true
}

func checkPossibility(nums []int) bool {
	n := len(nums)
	if n <= 1 {
		return true
	}

	tnums := make([]int, n)
	copy(tnums, nums)

	for i := 1; i < n; i++ {
		if nums[i] < nums[i - 1] {
			nums[i] = nums[i - 1]
			break
		}
	}

	if _checkPossibility(nums) {
		return true
	}

	nums = tnums
	for i := 1; i < n; i++ {
		if nums[i] < nums[i - 1] {
			nums[i - 1] = nums[i]
			break
		}
	}
	return _checkPossibility(nums)
}
