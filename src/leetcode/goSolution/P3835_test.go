package goSolution

import "testing"

func TestLargestIsland(t *testing.T) {
	grids := [][]int {{1, 0},{0, 1}}
	AssertEqual(t, 3, largestIsland(grids))

	grids = [][]int {{1, 1},{1, 0}}
	AssertEqual(t, 4, largestIsland(grids))

	grids = [][]int {{1, 1},{1, 1}}
	AssertEqual(t, 4, largestIsland(grids))
}
