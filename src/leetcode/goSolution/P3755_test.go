package goSolution

import "testing"

func TestEvalRPN(t *testing.T) {
	tokens := []string {"4","13","5","/","+"}
	AssertEqual(t, 6, evalRPN(tokens))
}
