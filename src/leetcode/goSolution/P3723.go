package goSolution

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	n := len(obstacleGrid)
	m := len(obstacleGrid[0])

	f := make([][]int, n + 1)
	for i := 0; i < n + 1; i++ {
		f[i] = make([]int, m + 1)
	}

	f[0][1] = 1
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if obstacleGrid[i][j] == 0 {
				f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
			}
		}
	}
	return f[n][m]
}
