package goSolution

import "testing"

func TestLongestStrChain(t *testing.T) {
	words := []string {"xbc","pcxbcf","xb","cxbc","pcxbc"}
	AssertEqual(t, 5, longestStrChain(words))
}
