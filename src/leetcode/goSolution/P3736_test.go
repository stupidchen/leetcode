package goSolution

import "testing"

func TestSuperpalindromesInRange(t *testing.T) {
	AssertEqual(t, 1, superpalindromesInRange("1", "1000000000000000000"))
	AssertEqual(t, 4, superpalindromesInRange("4", "1000"))
}
