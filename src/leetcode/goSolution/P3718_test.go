package goSolution

import "testing"

func TestCountBinarySubstringsNormalCase(t *testing.T) {
	AssertEqual(t, 	countBinarySubstrings("00110011"), 6)
}
