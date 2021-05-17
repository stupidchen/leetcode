package goSolution

func IsPredecessor(x, y string) bool {
	n := len(x)
	if len(y) != n + 1 {
		return false
	}
	t := 1
	for i, j := 0, 0; i < len(x); i, j = i + 1, j + 1 {
		if x[i] != y[j] {
			if t > 0 {
				t -= 1
				i -= 1
			} else {
				return false
			}
		}
	}
	return true
}

func longestStrChain(words []string) int {
	n := len(words)
	edges := make([][]int, n)
	v := make([]int, n)
	q := make([]int, n)
	for i := 0; i < n; i++ {
		edges[i] = make([]int, 0)
		v[i] = 1
		q[i] = i
	}

	for i, word0 := range words {
		for j, word1 := range words {
			if IsPredecessor(word0, word1) {
				edges[i] = append(edges[i], j)
			}
		}
	}

	for h := 0; h < len(q); h++ {
		c := q[h]
		for _, next := range edges[c] {
			if v[next] < v[c] + 1 {
				v[next] = v[c] + 1
				q = append(q, next)
			}
		}
	}

	return max(v...)
}
