package goSolution

import "testing"

func TestMinDistance(t *testing.T) {
	AssertEqual(t, 2, minDistance("sea", "eat"))
	AssertEqual(t, 4, minDistance("leetcode", "etco"))
}
