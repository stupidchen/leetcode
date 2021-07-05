package goSolution

func matrixReshape(mat [][]int, r int, c int) [][]int {
	ret := make([][]int, r)
	n := len(mat)
	m := len(mat[0])
	if n * m != r * c {
		return mat
	}
	for i := 0; i < r; i++ {
		ret[i] = make([]int, c)
		for j := 0; j < c; j++ {
			k := i * c + j
			ret[i][j] = mat[k / m][k % m]
		}
	}
	return ret
}
