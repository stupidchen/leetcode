package goSolution

import "testing"

func TestSuggestedProducts(t *testing.T) {
	AssertEqual(t, [][]string{
		{"mobile", "moneypot", "monitor"},
		{"mobile", "moneypot", "monitor"},
		{"mouse", "mousepad"},
		{"mouse", "mousepad"},
		{"mouse", "mousepad"}}, suggestedProducts([]string{"mobile","mouse","moneypot","monitor","mousepad"}, "mouse"))
}
