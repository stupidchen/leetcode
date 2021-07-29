package goSolution

func updateMatrix(mat [][]int) [][]int {
	n := len(mat)
	m := len(mat[0])
	ret := Initialize2DIntSlice(n, m, n + m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if mat[i][j] == 0 {
				ret[i][j] = 0
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if mat[i][j] == 0 {
				q := make([][]int, 0)
				q = append(q, []int{i, j})
				for h := 0; h < len(q); h++ {
					x, y := q[h][0], q[h][1]
					for k := 0; k < 4; k++ {
						tx, ty := x + DX[k], y + DY[k]
						if tx >= 0 && tx < n && ty >= 0 && ty < m && mat[tx][ty] == 1 && ret[tx][ty] > ret[x][y] + 1 {
							ret[tx][ty] = ret[x][y] + 1
							q = append(q, []int{tx, ty})
						}
					}
				}
			}
		}
	}
	return ret
}
