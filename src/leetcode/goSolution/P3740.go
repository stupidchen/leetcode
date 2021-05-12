package goSolution

type NumMatrix struct {
	n, m int
	s [][]int
}

// Remove ForNumMatrix before submit
func ConstructorForNumMatrix(matrix [][]int) NumMatrix {
	n := len(matrix)
	m := 0
	if n > 0 {
		m = len(matrix[0])
		s := make([][]int, n + 1)
		for i := 0; i < n + 1; i++ {
			s[i] = make([]int, m + 1)
		}
		for i := 0; i < n; i++ {
			for j := 0; j < m; j++ {
				s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] + matrix[i][j] - s[i][j]
			}
		}

		return NumMatrix{n: n, m: m, s: s}
	}
	return NumMatrix{}
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	if this.n == 0 {
		return 0
	}

	s := this.s
	return s[row2 + 1][col2 + 1] - s[row1][col2 + 1] - s[row2 + 1][col1] + s[row1][col1]
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
