package goSolution

func numMatchingSubseq(s string, words []string) int {
	n := len(s)
	m := len(words)
	f := make([]int, m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if f[j] < len(words[j]) && words[j][f[j]] == s[i] {
				f[j] += 1
			}
		}
	}

	ret := 0
	for i := 0; i < m; i++ {
		if f[i] == len(words[i]) {
			ret += 1
		}
	}
	return ret
}
