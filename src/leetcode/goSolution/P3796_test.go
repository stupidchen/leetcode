package goSolution

import "testing"

func TestLongestOnes(t *testing.T) {
	AssertEqual(t, 6, longestOnes([]int{1,1,1,0,0,0,1,1,1,1,0}, 2))
}
