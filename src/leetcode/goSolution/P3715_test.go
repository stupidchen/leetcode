package goSolution

import "testing"

func TestMinimumTotalNormalCase(t *testing.T) {
	triangle := [][]int {{2},{3,4},{6,5,7},{4,1,8,3}}
	AssertEqual(t, 	minimumTotal(triangle), 11)
}
