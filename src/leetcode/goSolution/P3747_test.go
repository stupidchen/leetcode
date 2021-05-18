package goSolution

import "testing"

func TestFindDuplicate(t *testing.T) {
	paths := []string {"root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"}
	AssertEqual(t, [][]string {{"root/a/1.txt","root/c/3.txt"}, {"root/a/2.txt","root/c/d/4.txt","root/4.txt"}}, findDuplicate(paths))
}
