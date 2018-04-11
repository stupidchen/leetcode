package leetcode

func singleNumber(nums []int) int {
	var b0 = 0
	var b1 = 0

	for i := 0; i < len(nums); i++ {
		b0 = (b0 ^ nums[i]) & ^b1
		b1 = (b1 ^ nums[i]) & ^b0
	}

	return b0
}