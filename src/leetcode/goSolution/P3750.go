package goSolution

func IsFitsPattern(str string, pattern string) bool {
	patternMap := make(map[byte]byte)
	charMap := make(map[byte]byte)
	for i, char := range str {
		charByte := byte(char)
		if patternMap[charByte] != 0 {
			if patternMap[charByte] != pattern[i] {
				return false
			}
		} else {
			if charMap[pattern[i]] != 0 {
				return false
			}
			charMap[pattern[i]] = charByte
			patternMap[charByte] = pattern[i]
		}
	}
	return true
}

func findAndReplacePattern(words []string, pattern string) []string {
	ret := make([]string, 0)
	for _, word := range words {
		if IsFitsPattern(word, pattern) {
			ret = append(ret, word)
		}
	}

	return ret
}
