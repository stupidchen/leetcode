package goSolution

import "testing"

func TestAmbiguousCoordinates(t *testing.T) {
	AssertEqual(t, []string{"(0, 0.011)", "(0.001, 1)"}, ambiguousCoordinates("(00011)"))
}
