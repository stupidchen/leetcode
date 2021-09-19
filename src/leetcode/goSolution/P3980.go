package goSolution

var f[10000][1000] int

func numDistinct(s string, t string) int {
	var lens = len(s)
	var lent = len(t)

	if lens == 0 || lent == 0 {
		return 0
	}

	for i := 0; i < lens; i++ {
		for j := 0; j < lent; j++ {
			f[i][j] = 0
			if s[i] == t[j] {
				if j == 0 {
					f[i][j] = 1
					continue
				}

				var tmp = 0
				for k := 0; k < i; k++ {
					tmp += f[k][j - 1]
				}
				if tmp > f[i][j] {
					f[i][j] = tmp
				}
			}
		}
	}

	var ret = 0
	for i := 0; i < lens; i++ {
		ret += f[i][lent - 1]
	}

	return ret
}
