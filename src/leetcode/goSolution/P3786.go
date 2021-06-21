package goSolution

func generate(numRows int) [][]int {
	a := make([][]int, numRows)
	a[0] = []int{1}
	if numRows > 1 {
		a[1] = []int{1, 1}
		for i := 2; i < numRows; i++ {
			a[i] = make([]int, i + 1)
			a[i][0] = 1
			for j := 1; j < i; j++ {
				a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
			}
			a[i][i] = 1
		}
	}
	return a
}
