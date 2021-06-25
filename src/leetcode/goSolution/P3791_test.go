package goSolution

import "testing"

func TestFindRedundantConnection(t *testing.T) {
	edges := [][]int {{1, 2},{3, 1}, {2, 3}}
	AssertEqual(t, []int{2, 3}, findRedundantConnection(edges))
}
