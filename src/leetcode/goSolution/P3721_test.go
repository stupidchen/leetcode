package goSolution

import "testing"

func TestFurthestBuilding(t *testing.T) {
	heights := []int {4,2,7,6,9,14,12}
	AssertEqual(t, 4, furthestBuilding(heights, 5, 1))

	heights = []int {4,12,2,7,3,18,20,3,19}
	AssertEqual(t, 7, furthestBuilding(heights, 10, 2))
}

