package goSolution

func maximumUniqueSubarray(nums []int) int {
	numsMap := make(map[int]bool)
	s := 0
	last := 0
	ret := 0
	for _, num := range nums {
		for ; numsMap[num]; last++ {
			numsMap[nums[last]] = false
			s -= nums[last]
		}
		numsMap[num] = true
		s += num
		ret = max(s, ret)
	}
	return ret
}
