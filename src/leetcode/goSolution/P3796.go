package goSolution

func longestOnes(nums []int, k int) int {
	ret := 0
	last := 0
	current := 0
	flip := 0
	for _, num := range nums {
		if num == 0 {
			flip++
		}
		current += 1
		for ; flip > k; last++ {
			if nums[last] == 0 {
				flip--
			}
			current--
		}
		ret = max(ret, current)
	}
	return ret
}
