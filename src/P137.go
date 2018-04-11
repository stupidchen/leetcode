package leetcode

import "fmt"

func singleNumber(nums []int) int {
	var f [128]int
	var s = 0

	for i := 0; i < len(nums); i++ {
		var j = 0
		if nums[i] < 0 {
			s++
			nums[i] = -nums[i]
		}
		for t := nums[i]; t > 0; t = t >> 1 {
			if (t & 1) == 1 {
				f[j]++
			}
			j++
		}
	}

	var ret = 0
	for i := 127; i >= 0; i--{
		f[i] %= 3
		ret = (ret << 1) + f[i]
	}

	if s % 3 != 0{
		ret = -ret
	}
	return ret
}

func main() {
	fmt.Println(singleNumber([]int {1}))
}