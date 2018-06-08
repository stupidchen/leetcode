package leetcode

const maxn = 4000
var wordMap [maxn][maxn]int
var wordLink [maxn][maxn]int
var wordDis [maxn]int
var wordQueue [maxn * 10]int
var ret [][]string
var minLen = -1
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

func solveLadders(d int, c int, curSol []int, wordList []string, beginWord string) {
	if c == n {
		tmpSol := make([]string, minLen)
		for i := 0; i < minLen; i++ {
			tmpSol[minLen - i - 1] = getWord(wordList, curSol[i], beginWord) + ""
		}

		ret = append(ret, tmpSol)
		return
	}
	for i := 1; i <= wordLink[c][0]; i++ {
		next := wordLink[c][i]
		curSol[d] = next
		solveLadders(d + 1, next, curSol, wordList, beginWord)
	}
}

func solveWordDis() {
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
				wordLink[next][0] = 0
			}
			if wordDis[next] == wordDis[i] + 1 {
				wordLink[next][0]++
				wordLink[next][wordLink[next][0]] = i
			}
		}
	}
}

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	n = len(wordList)
	ret = make([][]string, 0, n)
	if n == 0 {
		return ret
	}

	for i := 0; i <= n; i++ {
		wordMap[i][0] = 0
		wordLink[i][0] = 0
	}

	var target = -1
	for i := 0; i <= n; i++ {
		if wordDiffNum(getWord(wordList, i, beginWord), endWord) == 0 {
			target = i
		}
	}

	if target == -1 {
		return ret
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

	solveWordDis()

	if wordDis[target] > n {
		return ret
	}

	minLen = wordDis[target] + 1
	solution := make([]int, minLen)
	solution[0] = target
	solveLadders(1, target, solution, wordList, beginWord)
	return ret
}

func main() {
	findLadders("hit", "cog", []string{"hot", "dot", "dog", "lot", "log", "cog"})
}
