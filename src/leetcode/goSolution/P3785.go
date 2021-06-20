package goSolution

func canSwimToTheEnd(grid [][]int, t int) bool {
	n := len(grid)
	m := len(grid[0])
	q := [][]int{{0, 0}}
	v := Initialize2DIntSlice(n, m, -1)
	v[0][0] = 0
	for h := 0; h < len(q); h++ {
		x, y := q[h][0], q[h][1]
		for d := 0; d < 4; d++ {
			tx, ty := x + DX[d], y + DY[d]
			if tx >= 0 && ty >= 0 && tx < n && ty < m && v[tx][ty] == -1 && grid[tx][ty] <= t {
				q = append(q, []int{tx, ty})
				v[tx][ty] = v[x][y] + 1
			}
		}

		if v[n - 1][m - 1] != -1 {
			return true
		}
	}
	return false
}

func swimInWater(grid [][]int) int {
	maxTime := 0
	for _, row := range grid {
		maxTime = max(maxTime, max(row...))
	}

	var l, r int
	for l, r = grid[0][0], maxTime; l <= r; {
		mid := (l + r) >> 1
		if canSwimToTheEnd(grid, mid) {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return r + 1
}
