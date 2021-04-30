package goSolution

import "testing"

func TestPowerfulIntegers(t *testing.T) {
	AssertEqual(t, 7, len(powerfulIntegers(2, 3, 10)))
}
