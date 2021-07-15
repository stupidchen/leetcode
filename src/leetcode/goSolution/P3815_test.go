package goSolution

import "testing"

func TestTriangleNumber(t *testing.T) {
	AssertEqual(t, 4, triangleNumber([]int{4,3,2,4}))
}
