package leetcode

const maxn = 1000
var wordMap [maxn][maxn]int
var n int

func wordDiffNum(x string, y string) int {
	if len(x) != len(y) {
		return -1
	}

	var ret = 0
	for i := 0; i < len(x); i++ {
		if x[i] != y[i] {
			ret++
		}
	}

	return ret
}

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	n = len(wordList)
	var ret [][]string
	if n == 0 {
		return ret
	}
}