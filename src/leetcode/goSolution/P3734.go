package goSolution

func minDistance(word1 string, word2 string) int {
	n, m := len(word1), len(word2)
	f := make([][]int, n + 1)
	for i := 0; i < n + 1; i++ {
		f[i] = make([]int, m + 1)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])

			if word1[i] == word2[j] {
				f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + 1)
			}
		}
	}

	return n + m - (f[n][m] << 1)
}