package goSolution

func kInversePairs(n int, k int) int {
	m := k
	f := Initialize2DIntSlice(n + 1, m + 1, 0)
	for i := 1; i <= n; i++ {
		f[i][0] = 1
		s := 1
		for j := 1; j <= min(m, i * (i - 1) / 2); j++ {
			if j >= i {
				s -= f[i - 1][j - i]
			}
			s += f[i - 1][j]
			f[i][j] = s % MODULO
		}
	}

	return f[n][m]
}

