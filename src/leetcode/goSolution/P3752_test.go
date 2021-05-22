package goSolution

import "testing"

func TestSolveNQueens(t *testing.T) {
	answer := [][]string{{".Q..","...Q","Q...","..Q."},{"..Q.","Q...","...Q",".Q.."}}
	AssertEqual(t, answer, solveNQueens(4))
}
