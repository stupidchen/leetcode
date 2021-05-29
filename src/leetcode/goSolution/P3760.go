package goSolution

func totalNQueens(n int) int {
	ret := make([][]string, 0)
	columns := (1 << n) - 1 // y
	diag0 := 0 // x + y
	diag1 := 0 // x - y + n - 1
	board := make([][]bool, n)
	for i := 0; i < n; i++ {
		board[i] = make([]bool, n)
	}
	initLg2Map(n << 1)

	SolveNQueens(0, n, columns, diag0, diag1, board, &ret)
	return len(ret)
}
