func flipAndInvertImage(A [][]int) [][]int {
	var n = len(A)
	if n == 0 {
		return A
	}
	var m = len(A[0])
	for i := 0; i < n; i++ {
		for j := 0; j << 1 < m; j++ {
			var t = A[i][j]
			A[i][j] = 1 - A[i][m - j - 1]
			A[i][m - j - 1] = 1 - t
		}
	}
	return A
}