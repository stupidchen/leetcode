package leetcode

func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	charmap := make(map[byte]byte)
	ret := true
	for i := 0; i < len(s); i++ {
		c, e := charmap[s[i]]
		if !e {
			charmap[s[i]] = t[i]
		} else {
			if c != t[i] {
				ret = false
				break
			}
		}

	}
	if ret {
		charmap := make(map[byte]byte)
		for i := 0; i < len(t); i++ {
			c, e := charmap[t[i]]
			if !e {
				charmap[t[i]] = s[i]
			} else {
				if c != s[i] {
					ret = false
					break
				}
			}

		}
	}
	return ret
}