package goSolution

func pushDominoes(dominoes string) string {
	n := len(dominoes)
	rd := make([]int, n)
	ld := make([]int, n)
	lastL := -1
	for i := 0; i < n; i++ {
		if dominoes[i] == 'R' {
			lastL = i
			rd[i] = 1
		} else if dominoes[i] == 'L' {
			lastL = -1
			rd[i] = n + 1
		} else {
			if dominoes[i] == '.' && lastL != -1 {
				rd[i] = i - lastL + 1
			} else {
				rd[i] = n + 1
			}
		}
	}

	lastR := -1
	for i := n - 1; i >= 0; i-- {
		if dominoes[i] == 'L' {
			lastR = i
			ld[i] = 1
		} else if dominoes[i] == 'R' {
			lastR = -1
			ld[i] = n + 1
		} else {
			if dominoes[i] == '.' && lastR != -1 {
				ld[i] = lastR - i + 1
			} else {
				ld[i] = n + 1
			}
		}
	}

	ret := ""
	for i := 0; i < n; i++ {
		if ld[i] == rd[i] {
			ret += "."
		} else if ld[i] > rd[i] {
			ret += "R"
		} else {
			ret += "L"
		}
	}
	return ret
}
