package goSolution

import "testing"

func TestLeastBricksNormalCase(t *testing.T) {
	wall := [][]int {{1,2,2,1}, {3,1,2}, {1,3,2}, {2,4}, {3,1,2}, {1,3,1,1}}
	AssertEqual(t, 	leastBricks(wall), 2)
}
