package goSolution

import "testing"

func TestShortestSuperstring(t *testing.T) {
	words := []string {"catg","ctaagt","gcta","ttca","atgcatc"}
	AssertEqual(t, "gctaagttcatgcatc", shortestSuperstring(words))
}
