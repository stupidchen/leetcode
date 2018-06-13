package leetcode

func containsNearbyDuplicate(nums []int, k int) bool {
	n := len(nums)
	for i := 1; i < n; i++ {
		for j := i - 1; j >= i - k && j >= 0; j-- {
			if nums[i] == nums[j] {
				return true
			}
		}
	}
	return false
}