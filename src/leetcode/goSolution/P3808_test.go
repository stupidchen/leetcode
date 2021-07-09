package goSolution

import "testing"

func TestLengthOfLIS(t *testing.T) {
	AssertEqual(t, 4, lengthOfLIS([]int{10,9,2,5,3,7,101,18}))
}
