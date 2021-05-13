package goSolution

import (
	"fmt"
	"strconv"
	"strings"
)

func isFloat(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	m := len(s)
	t := strings.Index(s, ".")
	if t != -1 {
		if s[m - 1] == '0' {
			return false
		}
	}
	if err != nil || (len(s) >= 2 && (s[0] == '0' && s[1] != '.')) {
		return false
	}
	return true
}

func splitCoordinateNumber(s string) []string {
	ret := make([]string, 0)
	if isFloat(s) {
		ret = append(ret, s)
	}
	for i := 1; i < len(s); i++ {
		t := s[:i] + "." + s[i:]
		if isFloat(t) {
			ret = append(ret, t)
		}
	}
	return ret
}

func ambiguousCoordinates(s string) []string {
	s = s[1: len(s) - 1]
	n := len(s)
	ret := make([]string, 0)
	for i := 1; i < n; i++ {
		possibleX := splitCoordinateNumber(s[:i])
		possibleY := splitCoordinateNumber(s[i:])
		for _, x := range possibleX {
			for _, y := range possibleY {
				ret = append(ret, fmt.Sprintf("(%s, %s)", x, y))
			}
		}
	}

	return ret
}
