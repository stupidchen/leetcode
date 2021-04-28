package goSolution

import "testing"

func TestUniquePathsWithObstacles(t *testing.T) {
	grids := [][]int {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}
	AssertEqual(t, 2, uniquePathsWithObstacles(grids))
}
