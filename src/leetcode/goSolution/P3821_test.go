package goSolution

import "testing"

func TestPushDominoes(t *testing.T) {
	AssertEqual(t, "LL.RR" , pushDominoes(".L.R."))
	AssertEqual(t, "RR.LL" , pushDominoes("R...L"))
	AssertEqual(t, "RR.L" , pushDominoes("RR.L"))
}
