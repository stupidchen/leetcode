func solveParitition(s string, index int, ans *[][]string, sol []int, cur int) {
	if index >= len(s) {
		solStr := make([]string, cur)
		l := 0
		for i := 0; i < cur; i++ {
			solStr[i] = s[l: sol[i]]
			l = sol[i]
		}
		*ans = append(*ans, solStr)
		return
	}

	for i := 1; i + index <= len(s); i++ {
		can := true
		for r := i + index - 1; r > index; r-- {
			if s[r] != s[(index << 1) + i - 1 - r] {
				can = false
				break
			}
		}
		if can {
			sol[cur] = i + index
			solveParitition(s, i + index, ans, sol, cur + 1)
		}
	}
}

func partition(s string) [][]string {
	var ret = make([][]string, 0, len(s))
	var sol = make([]int, len(s) + 1, len(s) + 1)
	solveParitition(s, 0, &ret, sol, 0)
	return ret
}