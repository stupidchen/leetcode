package goSolution

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
	lastMatrix := Initialize2DIntSlice(n, m, 0)
	lastMatrix[startColumn][startRow] = 1

	var currentMatrix [][]int
	ret := 0
	for t := 0; t < maxMove; t++ {
		currentMatrix = Initialize2DIntSlice(n, m, 0)
		for i := 0; i < n; i++ {
			for j := 0; j < m; j++ {
				l := lastMatrix[i][j]
				for k := 0; k < 4; k++ {
					ti, tj := i + DX[k], j + DY[k]
					if (ti >= 0 && ti < n) && (tj >= 0 && tj < m) {
						currentMatrix[ti][tj] = (currentMatrix[ti][tj] + l) % MODULO
					} else {
						ret = (ret + l) % MODULO
					}
				}
			}
		}
		lastMatrix = currentMatrix
	}
	return ret
}
