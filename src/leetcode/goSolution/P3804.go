package goSolution

import "sort"

func minSetSize(arr []int) int {
	n := len(arr)
	s := make(map[int]int)
	for _, num := range arr {
		s[num]++
	}

	a := make([]int, 0)
	for _, v := range s {
		a = append(a, v)
	}
	sort.Ints(a)
	ret := 0
	sum := 0
	for i := len(a) - 1; i >= 0; i-- {
		if sum < n / 2 {
			ret += 1
			sum += a[i]
		} else {
			break
		}
	}
	return ret
}
