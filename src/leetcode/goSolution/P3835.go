package goSolution

func largestIsland(grid [][]int) int {
	n := len(grid)
	m := len(grid[0])
	gSet := Initialize2DIntSlice(n, m, 0)
	gSize := make(map[int]int)

	setNum := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if gSet[i][j] == 0 && grid[i][j] == 1 {
				setNum += 1
				q := [][]int {{i, j}}
				gSet[i][j] = setNum
				gSize[setNum] = 1
				for h := 0; h < len(q); h++ {
					x, y := q[h][0], q[h][1]
					for k := 0; k < 4; k++ {
						tx, ty := x + DX[k], y + DY[k]
						if tx >= 0 && tx < n && ty >= 0 && ty < m && gSet[tx][ty] == 0 && grid[tx][ty] == 1 {
							gSet[tx][ty] = setNum
							gSize[setNum]++
							q = append(q, []int{tx, ty})
						}
					}
				}
			}
		}
	}

	ret := 0
	for _, size := range gSize {
		ret = max(ret, size)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 0 {
				cSets := make(map[int]bool)
				for k := 0; k < 4; k++ {
					tx, ty := i+DX[k], j+DY[k]
					if tx >= 0 && tx < n && ty >= 0 && ty < m && gSet[tx][ty] != 0 {
						cSets[gSet[tx][ty]] = true
					}
				}

				c := 1
				for k, v := range cSets {
					if v {
						c += gSize[k]
					}
				}
				ret = max(ret, c)
			}
		}
	}
	return ret
}
