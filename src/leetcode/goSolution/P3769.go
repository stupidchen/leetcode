package goSolution

func longestConsecutive(nums []int) int {
	set := make(map[int]bool)
	for _, num := range nums {
		set[num] = true
	}

	ret := 0
	for _, num := range nums {
		if set[num] {
			t := 1
			for l := num - 1; set[l]; l-- {
				t += 1
				set[l] = false
			}

			for r := num + 1; set[r]; r++ {
				t += 1
				set[r] = false
			}
			ret = max(ret, t)
		}
	}
	return ret
}
