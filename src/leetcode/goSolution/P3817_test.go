package goSolution

import "testing"

func TestThreeEqualParts(t *testing.T) {
	AssertEqual(t, []int{15,32}, threeEqualParts([]int{1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0}))
}
