package goSolution

import "testing"

func TestSumOfFlooredPairs(t *testing.T) {
	nums := []int {2,5,9}
	AssertEqual(t, 10, sumOfFlooredPairs(nums))
}
