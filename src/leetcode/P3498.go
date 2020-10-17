import "strings"

func findRepeatedDnaSequences(s string) []string {
	var ans [1000]string
	var f = make(map[string]bool)
	var m = 0

	for i := 0; i < len(s) - 10; i++ {
		var t = s[i: i + 10]
		if strings.Contains(s[i + 1: ], t) && !f[t] {
			ans[m] = t
			f[t] = true
			m++
		}
	}

	return ans[0: m]
}
