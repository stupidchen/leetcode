package goSolution

func countVowelPermutation(n int) int {
	a, e, i, o, u := 1, 1, 1, 1, 1
	for k := 1; k < n; k++ {
		a, e, i, o, u = (e + i + u) % MODULO, (a + i) % MODULO, (e + o) % MODULO, i % MODULO, (i + o) % MODULO
	}
	return (a + e + i + o + u) % MODULO
}
