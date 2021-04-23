package goSolution

func countBinarySubstrings(s string) int {
	n := len(s)
	c := []int {0, 0}
	ret := 0
	for i := 1; i < n; i++ {
		c[0], c[1] = 0, 0
		for l, r := i - 1, i; l >= 0 && r < n; l, r = l - 1, r + 1 {
			if s[l] == '0' {
				c[0] += 1
			} else {
				c[1] += 1
			}

			if s[r] == '0' {
				c[0] += 1
			} else {
				c[1] += 1
			}

			if c[0] == c[1] && s[l] == s[i - 1] && s[r] == s[i] {
				ret += 1
			} else {
				break
			}
		}
	}

	return ret
}
