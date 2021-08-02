package goSolution

func twoSum(nums []int, target int) []int {
	numSet := make(map[int]int)
	for i, num := range nums {
		if numSet[num] != 0 {
			if target == num << 1 {
				return []int{numSet[num] - 1, i}
			}
		} else {
			if numSet[target - num] != 0 {
				return []int{numSet[target - num] - 1, i}
			}
			numSet[num] = i + 1
		}
	}
	return []int{-1, -1}
}
