package goSolution

import (
	"reflect"
	"runtime/debug"
	"testing"
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
