package goSolution

import "testing"

func TestThreeSumClosest(t *testing.T) {
	AssertEqual(t, 2, threeSumClosest([]int{-1,2,1,-4}, 1))
}
