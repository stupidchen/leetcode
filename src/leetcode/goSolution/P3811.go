package goSolution

func isIsomorphic(s string, t string) bool {
	set := make(map[rune]rune)
	rset := make(map[rune]rune)
	for i, c := range s {
		g := int32(t[i])
		k := set[c]
		rk := rset[g]
		if (k != 0 && g != k) || (rk != 0 && rk != c) {
			return false
		}
		set[c] = g
		rset[g] = c
	}
	return true
}
