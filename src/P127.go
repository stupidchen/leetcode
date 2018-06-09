package leetcode

const maxn = 5000
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

func getWord(wordList []string, index int, firstWord string) string {
	if index == len(wordList) {
		return firstWord
	}
	return wordList[index]
}

func solveWordDisWithPath(target int) int {
	var wordDis [maxn]int
	var wordQueue [maxn]int
	var h, t int
	h = 0
	t = 0
	wordQueue[0] = n
	for i := 0; i < n; i++ {
		wordDis[i] = n * n
	}
	wordDis[n] = 0
	for ; h <= t; h++ {
		i := wordQueue[h]
		for j := 1; j <= wordMap[i][0]; j++ {
			next := wordMap[i][j]
			if wordDis[next] > wordDis[i] + 1 {
				t++
				wordQueue[t] = next
				wordDis[next] = wordDis[i] + 1
			}
		}
	}

	return wordDis[target]
}


func ladderLength(beginWord string, endWord string, wordList []string) int {
	n = len(wordList)
	if n == 0 {
		return 0
	}

	for i := 0; i <= n; i++ {
		wordMap[i][0] = 0
	}

	var target = -1
	for i := 0; i <= n; i++ {
		if wordDiffNum(getWord(wordList, i, beginWord), endWord) == 0 {
			target = i
		}
	}

	if target == -1 {
		return 0
	}
	for i := 0; i <= n; i++ {
		for j := i + 1; j <= n; j++ {
			str0 := getWord(wordList, i, beginWord)
			str1 := getWord(wordList, j, beginWord)
			if wordDiffNum(str0, str1) == 1 {
				wordMap[i][0]++
				wordMap[j][0]++
				wordMap[i][wordMap[i][0]] = j
				wordMap[j][wordMap[j][0]] = i
			}
		}
	}

	ret := solveWordDisWithPath(target)
	if ret > n {
		ret = 0
	} else {
		ret++
	}
	return ret
}