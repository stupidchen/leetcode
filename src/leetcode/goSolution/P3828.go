package goSolution

import (
	"sort"
)

func IntAbs(x int) int {
	if x < 0 {
		x = -x
	}
	return x
}

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	n := len(nums)
	ret := nums[0] + nums[1] + nums[2]
	start := 2
	for k := 3; k < n; k++ {
		if IntAbs(nums[0] + nums[1] + nums[k] - target) < IntAbs(ret - target) {
			start = k
			ret = nums[0] + nums[1] + nums[k]
		}
	}


	for i := 0; i < n; i++ {
		if start <= i {
			start = i + 1
		}
		k := start
		for j := i + 1; j < n - 1; j++ {
			if k <= j {
				k = j + 1
			}
			tmp := nums[i] + nums[j] + nums[k]

			for l := k - 1; l > j; l-- {
				if IntAbs(nums[i] + nums[j] + nums[l] - target) < IntAbs(tmp - target) {
					tmp = nums[i] + nums[j] + nums[l]
					k = l
				} else {
					break
				}
			}

			for r := k + 1; r < n; r++ {
				if IntAbs(nums[i] + nums[j] + nums[r] - target) < IntAbs(tmp - target) {
					tmp = nums[i] + nums[j] + nums[r]
					k = r
				} else {
					break
				}
			}

			if IntAbs(tmp - target) < IntAbs(ret - target) {
				ret = tmp
			}
		}
	}
	return ret
}
