package goSolution

func rotate(matrix [][]int)  {
	n := len(matrix)
	m := n - 1
	if n & 1 == 1 {
		for i := 0; i <= n >> 1; i++ {
			for j := i; j < n - i - 1; j++ {
				matrix[i][j], matrix[j][m - i], matrix[m - i][m - j], matrix[m - j][i] = matrix[m - j][i], matrix[i][j], matrix[j][m - i], matrix[m - i][m - j]
			}
		}
	} else {
		for i := 0; i < n >> 1; i++ {
			for j := 0; j < n >> 1; j++ {
				matrix[i][j], matrix[j][m - i], matrix[m - i][m - j], matrix[m - j][i] = matrix[m - j][i], matrix[i][j], matrix[j][m - i], matrix[m - i][m - j]
			}
		}
	}
}
