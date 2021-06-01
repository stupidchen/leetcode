package goSolution

func maxAreaOfIsland(grid [][]int) int {
	n, m := len(grid), len(grid[0])

	t := 1
	ret := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 1 {
				q := [][]int{{i, j}}
				t += 1
				grid[i][j] = t
				for h := 0; h < len(q); h++ {
					x, y := q[h][0], q[h][1]
					for d := 0; d < 4; d++ {
						tx, ty := x + DX[d], y + DY[d]
						if 0 <= tx && tx < n && 0 <= ty && ty < m && grid[tx][ty] == 1 {
							grid[tx][ty] = t
							q = append(q, []int{tx, ty})
						}
					}
				}
				ret = max(ret, len(q))
			}
		}
	}

	return ret
}
