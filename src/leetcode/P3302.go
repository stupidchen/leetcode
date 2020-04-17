var dx = [4]int{1, -1, 0, 0}
var dy = [4]int{0, 0, 1, -1}

func floodIsland(grid [][]byte, x int, y int, n int, m int) {
	grid[x][y] = 'x'
	var tx, ty int
	for k := 0; k < 4; k++ {
		tx = x + dx[k]
		ty = y + dy[k]
		if tx >= 0 && ty >= 0 && tx < n && ty < m {
			if grid[tx][ty] == '0' {
				continue
			}
			if grid[tx][ty] == '1' {
				floodIsland(grid, tx, ty, n, m)
			}
		}
	}
}

func numIslands(grid [][]byte) int {
	var ans = 0
	var n = len(grid)
	if n == 0 {
		return ans
	}
	var m = len(grid[0])
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == '1' {
				floodIsland(grid, i, j, n, m)
				ans++
			}
		}
	}

	return ans
}