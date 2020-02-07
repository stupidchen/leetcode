package leetcode

var dx = []int{1, -1, 0, 0}
var dy = []int{0, 0, 1, -1}

func flip(board [][]byte, x int, y int) {
	if x < 0 || y < 0 || x >= len(board) ||  y >= len(board[0]) {
		return
	}
	if board[x][y] != 'O' {
		return
	} else {
		board[x][y] = 'A'
	}

	for i := 0; i < 4; i++ {
		flip(board, x + dx[i], y + dy[i])
	}
}

func solveSurroundedRegions(board [][]byte)  {
	n := len(board)
	if n == 0 {
		return
	}
	m := len(board[0])
	for i := 0; i < n; i++ {
		flip(board, i, 0)
		flip(board, i, m - 1)
	}
	for i := 0; i < m; i++ {
		flip(board, 0, i)
		flip(board, n - 1, i)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if board[i][j] == 'O' {
				board[i][j] = 'X'
			}
			if board[i][j] == 'A' {
				board[i][j] = 'O'
			}
		}
	}
}