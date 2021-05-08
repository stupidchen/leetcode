package goSolution

import (
	"strconv"
)

func superpalindromesInRange(left string, right string) int {
	ret := 0
	li, _ := strconv.Atoi(left)
	ri, _ := strconv.Atoi(right)

	for i := 1; ; i++ {
		s := strconv.Itoa(i)
		s = s + ReverseString(s)
		n, _ := strconv.Atoi(s)
		n = n * n
		if n <= ri {
			if n >= li && IsPalindrome(strconv.Itoa(n)) {
				ret += 1
			}
		} else {
			break
		}
	}

	for i := 0; ; i++ {
		s := strconv.Itoa(i)
		s = s + ReverseString(s[:len(s) - 1])
		n, _ := strconv.Atoi(s)
		n = n * n
		if n <= ri {
			if n >= li && IsPalindrome(strconv.Itoa(n)) {
				ret += 1
			}
		} else {
			break
		}
	}

	return ret
}
