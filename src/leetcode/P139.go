package leetcode

func wordBreak(s string, wordDict []string) bool {
	dict := make(map[string]bool)
	for i := range wordDict {
		dict[wordDict[i]] = true
	}


	f := make([]bool, len(s) + 1)
	f[0] = true
	for i := 0; i < len(s); i++ {
		f[i + 1] = false
		for j := 0; j < i; j++ {
			if f[j] {
				t := s[j: i + 1]
				if _, ok := dict[t]; ok {
					f[i + 1] = true
					break
				}
			}
		}
	}

	return f[len(s)]
}