package goSolution

import "testing"

func TestGenerateParenthesis(t *testing.T) {
	AssertEqual(t, []string{"((()))","(()())","(())()","()(())","()()()"}, generateParenthesis(3))
}
