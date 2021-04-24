package goSolution

import "testing"

func TestCriticalConnections(t *testing.T) {
	edges := [][]int {{0, 1}, {1, 2}, {2, 0}, {1, 3}}
	AssertEqual(t, 	criticalConnections(4, edges), [][]int {{1, 3}})
}
