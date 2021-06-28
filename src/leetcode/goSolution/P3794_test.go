package goSolution

import "testing"

func TestRemoveDuplicates(t *testing.T) {
	AssertEqual(t, "ca", removeDuplicates("abbaca"))
}
