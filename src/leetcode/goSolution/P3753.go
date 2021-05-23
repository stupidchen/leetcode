package goSolution

func countSaveChar(x, y string) int {
	ret := 0
	lx, ly := len(x), len(y)
	for i := 0; i < min(lx, ly); i++ {
		if x[lx-i-1:] == y[:i+1] {
			ret = i + 1
		}
	}
	return ret
}

func fOfSaveChar(status int, last int, statusMap [][]int, saveChar [][]int) int {
	if statusMap[status][last] != -1 {
		return statusMap[status][last]
	}
	ret := 0
	if status != 0 {
		updatedStatus := status - (1 << last)
		for t := updatedStatus; t > 0; {
			b := GetLastBit(t)
			i := lg2(b)
			ret = max(ret, fOfSaveChar(updatedStatus, i, statusMap, saveChar) + saveChar[i][last])
			t -= b
		}
	}
	statusMap[status][last] = ret
	return ret
}

func shortestSuperstring(words []string) string {
	n := len(words)
	c := Initialize2DIntSlice(n, n, 0)
	for i, wordI := range words {
		for j, wordJ := range words {
			c[i][j] = countSaveChar(wordI, wordJ)
		}
	}

	m := 1 << n
	statusMap := Initialize2DIntSlice(m, n, -1)
	initLg2Map(n)
	maxSaveChar := 0
	for i := 0; i < n; i++ {
		maxSaveChar = max(fOfSaveChar(m - 1, i, statusMap, c), maxSaveChar)
	}

	status := m - 1
	order := make([]int, n)
	last := -1
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			t := statusMap[status][j]
			if last != -1 {
				t += c[j][last]
			}
			if maxSaveChar == t && status | (1 << j) == status {
				order[n - i - 1] = j
				if last != -1 {
					maxSaveChar -= c[j][last]
				}
				status -= 1 << j
				last = j
				break
			}
		}
	}

	ret := words[order[0]]
	for i := 1; i < n; i++ {
		ret = ret + words[order[i]][c[order[i - 1]][order[i]]:]
	}
	return ret
}
