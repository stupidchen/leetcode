package goSolution

import (
	"reflect"
	"runtime/debug"
	"strings"
	"testing"
	"unicode/utf8"
)

func AssertEqual(t *testing.T, b interface{}, a interface{}) {
	if reflect.DeepEqual(a, b) {
		return
	}
	debug.PrintStack()
	t.Errorf("Received %v (type %v), expected %v (type %v)", a, reflect.TypeOf(a), b, reflect.TypeOf(b))
}

func max(vars ...int) int {
	r := vars[0]
	for i := 1; i < len(vars); i++ {
		if r < vars[i] {
			r = vars[i]
		}
	}
	return r
}

func min(vars ...int) int {
	r := vars[0]
	for i := 1; i < len(vars); i++ {
		if r > vars[i] {
			r = vars[i]
		}
	}
	return r
}

func ReverseString(s string) string {
	size := len(s)
	buf := make([]byte, size)
	for start := 0; start < size; {
		r, n := utf8.DecodeRuneInString(s[start:])
		start += n
		utf8.EncodeRune(buf[size-start:], r)
	}
	return string(buf)
}

func CompareStringAsInt(x, y string) int {
	if len(x) < len(y) {
		return -1
	}

	if len(x) > len(y) {
		return 1
	}

	return strings.Compare(x, y)
}

func IsPalindrome(s string) bool {
	n := len(s)
	for i := 0; i < n>>1; i++ {
		if s[i] != s[n-i-1] {
			return false
		}
	}
	return true
}

func sum(a []int) int {
	ret := 0
	for _, v := range a {
		ret += v
	}
	return ret
}
