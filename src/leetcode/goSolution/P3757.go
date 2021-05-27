package goSolution

func maxProduct(words []string) int {
	n := len(words)
	chars := make([]map[rune]bool, n)
	for i, word := range words {
		chars[i] = make(map[rune]bool)
		for _, char := range word {
			chars[i][char] = true
		}
	}


	ret := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			shareCommonChar := false
			for k, _ := range chars[i] {
				if chars[j][k] {
					shareCommonChar = true
					break
				}
			}
			if !shareCommonChar {
				ret = max(ret, len(words[i]) * len(words[j]))
			}
		}
	}
	return ret
}
