package goSolution

import "math"

func powerfulIntegers(x int, y int, bound int) []int {
	t := make(map[int]bool, bound)
	for i := 0; ; i++ {
		c := true
		for j := 0; ; j++ {
			k := int(math.Pow(float64(x), float64(i))) + int(math.Pow(float64(y), float64(j)))
			if k > bound {
				break
			}
			c = false
			t[k] = true
			if y == 1 {
				break
			}
		}
		if c || x == 1 {
			break
		}
	}

	ret := []int{}
	for k, _ := range t {
		ret = append(ret, k)
	}
	return ret
}
