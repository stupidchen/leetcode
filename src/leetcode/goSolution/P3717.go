package goSolution

func leastBricks(wall [][]int) int {
	f := make(map[int]int)
	n := len(wall)
	for i := 0; i < n; i++ {
		w := wall[i]
		k := 0
		for j := 0; j < len(w) - 1; j++ {
			k += w[j]
			f[k] += 1
		}
	}

	r := 0
	for _, value := range f {
		r = max(r, value)
	}
	return n - r
}

