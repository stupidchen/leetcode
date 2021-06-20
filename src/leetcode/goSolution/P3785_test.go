package goSolution

import "testing"

func TestSwimInWater(t *testing.T) {
	grid := [][]int {{3, 2},{0, 1}}
	AssertEqual(t, 3, swimInWater(grid))
}
