package goSolution

import (
	"reflect"
	"runtime/debug"
	"strconv"
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

func GetPrefixSum(a []int) []int {
	n := len(a)
	ret := make([]int, n + 1)
	for i, v := range a {
		ret[i + 1] = ret[i] + v
	}
	return ret
}

func GetLastBit(x int) int {
	return x ^ (x & (x - 1))
}

var LG2MAP = make(map[int]int)

var DX = []int{1, -1, 0, 0, 1, 1, -1, -1}
var DY = []int{0, 0, 1, -1, 1, -1, 1, -1}

func initLg2Map(n int) {
	p := 1
	for i := 0; i < n; i++ {
		LG2MAP[p] = i + 1
		p = p << 1
	}
}

func lg2(x int) int {
	return LG2MAP[x] - 1
}

func Initialize2DIntSlice(n, m, v int) [][]int {
	ret := make([][]int, n)
	for i := 0; i < n; i++ {
		ret[i] = make([]int, m)
		for j := 0; j < m; j++ {
			ret[i][j] = v
		}
	}
	return ret
}

func Initialize2DBoolSlice(n, m int, v bool) [][]bool {
	ret := make([][]bool, n)
	for i := 0; i < n; i++ {
		ret[i] = make([]bool, m)
		for j := 0; j < m; j++ {
			ret[i][j] = v
		}
	}
	return ret
}

func IsNumeric(x string) bool {
	_, err := strconv.ParseInt(x, 10, 64)
	if err != nil {
		return false
	}
	return true
}

const MODULO = 1000000007