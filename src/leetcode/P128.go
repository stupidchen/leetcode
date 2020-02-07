package leetcode

import "fmt"

func longestConsecutive(nums []int) int {
	f := make(map[int]int)
	ret := 0
	for i := 0; i < len(nums); i++ {
		f[nums[i]] = 1
	}
	for i := 0; i < len(nums); i++ {
		if _, e := f[nums[i] - 1]; !e {
			var t int
			for t = 0; ; t++ {
				if _, e := f[nums[i] + t]; !e {
					break
				}
			}
			if t > ret {
				ret = t
			}
		}
	}
	return ret
}

func main() {
	fmt.Println(longestConsecutive([]int {100,4,200,1,3,2,201,101,203,99,98,204,202}))
}