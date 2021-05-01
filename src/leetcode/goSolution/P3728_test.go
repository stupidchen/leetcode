package goSolution

import "testing"

func TestWordFilter_F(t *testing.T) {
	wf := Constructor([]string{"apple", "banana", "bana"})
	AssertEqual(t, 0, wf.F("a", "e"))
	AssertEqual(t, 0, wf.F("", "e"))
	AssertEqual(t, 2, wf.F("", ""))
	AssertEqual(t, 2, wf.F("b", "na"))
	AssertEqual(t, 1, wf.F("b", "banana"))
	AssertEqual(t, -1, wf.F("b", "canana"))
	AssertEqual(t, 1, wf.F("b", "nana"))
}
