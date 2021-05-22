package goSolution

func GetBoardString(board [][]bool, n int) []string {
	ret := make([]string, n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] {
				ret[i] += "Q"
			} else {
				ret[i] += "."
			}
		}
	}
	return ret
}

func SolveNQueens(row int, n int, columns, diag0, diag1 int, board [][]bool, answers *[][]string) {
	if row == n {
		*answers = append(*answers, GetBoardString(board, n))
		return
	}

	for t := columns; t > 0; {
		b := GetLastBit(t)
		column := lg2(b)
		updatedDiag0 := diag0 | (1 << (row + column))
		updatedDiag1 := diag1 | (1 << (row - column + n - 1))
		if updatedDiag0 != diag0 && updatedDiag1 != diag1 {
			board[row][column] = true
			SolveNQueens(row + 1, n, columns - b, updatedDiag0, updatedDiag1, board, answers)
			board[row][column] = false
		}
		t -= b
	}
}

func solveNQueens(n int) [][]string {
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
	return ret
}
