package leetcode

func rob(nums []int) int {
	var prev = 0
	var last = 0
	var ret = 0

	for i := 0; i < len(nums); i++ {
		if prev + nums[i] > ret {
			ret = prev + nums[i]
		}
		prev = last
		last = ret
	}

	return ret
}